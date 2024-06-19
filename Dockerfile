# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# List the contents of /app to ensure requirements.txt is copied
RUN ls -l /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY app/ /app/

# List the contents of /app to ensure all files are copied
RUN ls -l /app
RUN ls -l /app/templates
RUN ls -l /app/static

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run main.py when the container launches
CMD ["python", "app/main.py"]
