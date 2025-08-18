#swagger.py
from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = Flask(__name__)

# Set up Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yml'

# Serve the swagger.yml file
@app.route('/static/<path:filename>')
def serve_static_file(filename):
    return send_from_directory(os.getcwd(), filename)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Swagger API Demo"
    }
)

# Register the Swagger UI Blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    # Read host and port from environment variables, with defaults
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', '5000'))
    app.run(debug=True, host=host, port=port)