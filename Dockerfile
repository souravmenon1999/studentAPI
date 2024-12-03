# Use the official Python 3.12 image
FROM python:3.12-slim

# Set working directory to cosmocloud
WORKDIR /cosmocloud

# Copy the current directory contents into the container
COPY . /cosmocloud/

# Install dependencies (no-cache-dir means no caching, keeping the image smaller)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will use, this can be read from the environment during runtime
# EXPOSE 8000 
EXPOSE ${PORT:-8000}

# Command to run the app (using the environment variable for port)
CMD ["python", "main.py"]
