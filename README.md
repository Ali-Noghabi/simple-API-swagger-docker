# Simple API-Swagger-Docker

A minimal, reusable template for serving a Python Flask API with Swagger UI for interactive documentation and automated unit tests, all containerized using Docker and Docker Compose. This project separates the API server and Swagger UI into two services, making it easy to replace the sample Flask app with your own webserver while keeping the Swagger UI consistent. It's a clean example of Docker multi-service setup, dependency management, and API testing.

## Features
- **Flask API**: A simple Flask server with sample GET and POST endpoints.
- **Swagger UI**: Interactive API documentation served from a `swagger.yml` file.
- **Unit Tests**: Automated tests for API endpoints using `pytest`.
- **Dockerized Services**: Separate Dockerfiles for the API server and Swagger UI, managed by Docker Compose.
- **Customizable**: Easily modify the API server (`src/app.py`) and its dependencies (`src/requirements.txt`) without affecting Swagger UI.

## Project Structure
```
.
├── docker-compose.yml         # Defines API and Swagger UI services
├── Dockerfile                 # For Swagger UI service
├── requirements.txt           # Dependencies for Swagger UI
├── src
│   ├── app.py                 # Sample Flask API
│   ├── Dockerfile.webserver   # For API server
│   ├── requirements.txt        # API server dependencies
│   └── test_api.py            # Unit tests for API
├── static
│   └── swagger.yml            # API definition for Swagger UI
└── swagger.py                 # Flask app for Swagger UI
```

## Setup and Running
1. **Clone the Project**:
   ```
   git clone <your-repo-url>
   cd simple-api-swagger-docker
   ```

2. **Build and Run**:
   ```
   docker-compose up --build
   ```
   - Builds and starts two containers: `swagger-ui-container` (port 5000) and `api-server-container` (port 5001).
   - Unit tests run automatically in `api-server-container`.
   - Access Swagger UI at `http://localhost:5000/swagger`.
   - Test APIs at `http://localhost:5001/api/v1/...` (e.g., `http://localhost:5001/api/v1/sample-get-api/John`).

3. **Stop Containers**:
   ```
   docker-compose down
   ```

## Testing
- **Automated Tests**: The `api-server` runs `pytest test_api.py` on startup. Check logs for results:
  ```
  docker-compose logs api-server-container
  ```
- **Manual Testing**:
  - Use curl:
    ```
    curl http://localhost:5001/api/v1/sample-get-api/John
    curl http://localhost:5001/api/v1/sample-get-api-query?name=John
    curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe"}' http://localhost:5001/api/v1/sample-post-api
    ```
  - Use Swagger UI at `http://localhost:5000/swagger` to interact with APIs.

## Customization
- **Update APIs**: Edit `src/app.py` for new endpoints and update `static/swagger.yml` to match.
- **Add Dependencies**: Modify `src/requirements.txt` (e.g., add `requests==2.26.0`) and rebuild.
- **Change Ports**: If 5000 or 5001 are in use, edit `ports` in `docker-compose.yml` (e.g., `5050:5000`).

## Troubleshooting
- **CORS Issues**: If Swagger UI shows CORS errors, verify `Access-Control-Allow-Origin` headers:
  ```
  curl -v -H "Origin: http://localhost:5000" http://localhost:5001/api/v1/sample-get-api/John
  ```
- **Container Exits**: Check logs (`docker-compose logs api-server-container`). Ensure tests pass or edit `docker-compose.yml` to use `;` instead of `&&` in the `api-server` command.
- **Port Conflicts**: Check with `netstat -tuln | grep -E '5000|5001'` and update `docker-compose.yml`.
- **Swagger UI Failure**: Ensure `http://localhost:5000/static/swagger.yml` is accessible.

## License
MIT License (create a `LICENSE` file if needed).

This project is a simple starting point for building and documenting APIs with Docker. Extend it by customizing `src/app.py` and `static/swagger.yml` for your needs!