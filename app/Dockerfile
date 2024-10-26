FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the Flask app
CMD ["python", "serve_model.py"]