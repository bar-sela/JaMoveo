# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY .. /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000


# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]