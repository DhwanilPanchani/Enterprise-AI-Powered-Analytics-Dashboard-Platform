# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# # Define the command to run your app
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# # ... all other lines remain the same ...

# Use Gunicorn to run the app in production
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "user_service.user_service.wsgi"]