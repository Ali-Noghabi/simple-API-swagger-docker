FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files for the Swagger UI service
COPY swagger.py /app/
COPY static /app/static
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port for the Swagger UI service
EXPOSE 5000

# Command to run the Swagger UI service
CMD ["python", "swagger.py"]