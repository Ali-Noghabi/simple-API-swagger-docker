# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000"}})

# Sample GET API with URL Parameter
@app.route('/api/v1/sample-get-api/<string:name>', methods=['GET'])
def sample_get_api(name):
    return jsonify({"message": f"Hello {name}!"})

# Sample GET API with Query Parameter
@app.route('/api/v1/sample-get-api-query', methods=['GET'])
def sample_get_api_query():
    name = request.args.get('name', '')
    return jsonify({"message": f"Hello {name}!"})

# Sample POST API
@app.route('/api/v1/sample-post-api', methods=['POST'])
def sample_post_api():
    data = request.get_json()
    name = data.get('name', '')
    return jsonify({'status': 'success', 'message': f'Received {name}'})

if __name__ == '__main__':
    # Read host and port from environment variables, with defaults
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', '5001'))
    app.run(debug=True, host=host, port=port)