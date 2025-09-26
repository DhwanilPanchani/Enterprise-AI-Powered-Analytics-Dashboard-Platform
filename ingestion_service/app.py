# File: ingestion_service/app.py

from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
import jwt
from functools import wraps
from flask_cors import CORS
import requests
import json
from bson import json_util # Helps convert MongoDB docs to JSON

app = Flask(__name__)
CORS(app)

# --- Configurations ---
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# --- Database Connection ---
client = MongoClient('mongodb://db-data:27017/')
db = client.analytics_db

# --- Simple Data Analysis Function (Free Alternative) ---
def analyze_data_simple(data, question):
    """
    Simple rule-based data analysis without requiring API keys
    """
    if not data:
        return "No data available for analysis."
    
    question_lower = question.lower()
    
    # Count total records
    total_records = len(data)
    
    # Analyze sales data
    if 'sale' in question_lower or 'sales' in question_lower:
        sales_count = sum(1 for item in data if item.get('event_type') == 'sale')
        return f"Found {sales_count} sales out of {total_records} total records."
    
    # Analyze by product
    if 'product' in question_lower:
        products = {}
        for item in data:
            if 'product_id' in item:
                product_id = item['product_id']
                products[product_id] = products.get(product_id, 0) + 1
        
        if products:
            top_product = max(products.items(), key=lambda x: x[1])
            return f"Product {top_product[0]} has the most activity with {top_product[1]} events."
        else:
            return "No product data found."
    
    # Analyze by date/time
    if 'date' in question_lower or 'time' in question_lower:
        dates = [item.get('timestamp') for item in data if 'timestamp' in item]
        if dates:
            return f"Data spans from {min(dates)} to {max(dates)} with {total_records} total records."
        else:
            return f"Found {total_records} records but no timestamp information."
    
    # General summary
    return f"Found {total_records} total records in the database. Ask about sales, products, or dates for more specific analysis."

# --- Authentication Decorator (unchanged) ---
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            token = token.split(" ")[1]
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except Exception as e:
            return jsonify({'message': 'Token is invalid or expired!'}), 401
        return f(*args, **kwargs)
    return decorated

# --- API Endpoints ---
@app.route('/api/ingest/health')
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/api/ingest', methods=['POST'])
def ingest_data():
    try:
        data = request.get_json()
        if not data: return jsonify({"error": "Invalid JSON"}), 400
        db.raw_data.insert_one(data)
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/data', methods=['GET'])
@token_required
def get_data():
    try:
        all_data = list(db.raw_data.find({}, {'_id': 0}))
        return jsonify(all_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- NEW AI-POWERED ENDPOINT ---
@app.route('/api/nlq', methods=['POST'])
@token_required
def natural_language_query():
    """
    Accepts a natural language question, fetches data, and asks the LLM for an answer.
    """
    try:
        # 1. Get the user's question from the request
        user_question = request.get_json().get('question')
        if not user_question:
            return jsonify({"error": "No question provided"}), 400

        # 2. Fetch all raw data from MongoDB
        all_data = list(db.raw_data.find())
        data_as_json = json.dumps(all_data, default=json_util.default)

        # 3. Create a prompt for the OpenAI model
        prompt = f"""
        You are a helpful data analyst. Your task is to answer a user's question based on the following JSON data.
        Provide a clear, concise, one or two-sentence answer.

        DATA:
        {data_as_json}

        QUESTION:
        {user_question}

        ANSWER:
        """
        
        # 4. Use a simple rule-based response (free alternative)
        # This provides basic data analysis without requiring API keys
        answer = analyze_data_simple(all_data, user_question)
        return jsonify({"answer": answer}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)