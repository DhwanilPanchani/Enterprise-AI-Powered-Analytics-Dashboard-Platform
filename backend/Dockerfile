# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY backend/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY backend/ .

# Set production environment variables
# IMPORTANT: Replace these placeholder values with your actual production keys.
ENV DJANGO_SECRET_KEY='django-insecure-6we_unvi*n(^hv5vj%2t$ru@5!0dpl&x@af-0vchku=^s^#al&'
ENV DATABASE_URL='postgresql://neondb_owner:npg_aR4spbefuw2z@ep-hidden-dream-advnpid6-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

# Expose the port the app runs on
EXPOSE 8000

# # Define the command to run your app
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# # ... all other lines remain the same ...

# Use Gunicorn to run the app in production
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "/app/user_service", "user_service.wsgi"]