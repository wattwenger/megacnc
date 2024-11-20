# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations
RUN python manage.py migrate

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dashboard.wsgi:application"]












# Use an official Python runtime as a parent image
#3FROM python:3.11

# Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
#WORKDIR /app

# Install dependencies
#COPY requirements.txt /app/
#RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
#COPY . /app/

# Command to run the application
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dashboard.wsgi:application"]
