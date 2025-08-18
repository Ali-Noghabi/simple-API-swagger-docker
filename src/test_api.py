import unittest
from app import app 

class TestSampleAPI(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_get_api_with_url_param(self):
        # Test GET /api/v1/sample-get-api/<name>
        response = self.app.get('/api/v1/sample-get-api/John')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello John!"})

    def test_get_api_with_query_param(self):
        # Test GET /api/v1/sample-get-api-query?name=John
        response = self.app.get('/api/v1/sample-get-api-query?name=John')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello John!"})

    def test_get_api_with_empty_query_param(self):
        # Test GET /api/v1/sample-get-api-query with no name
        response = self.app.get('/api/v1/sample-get-api-query')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello !"})

    def test_post_api(self):
        # Test POST /api/v1/sample-post-api
        response = self.app.post(
            '/api/v1/sample-post-api',
            json={"name": "John Doe"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "success", "message": "Received John Doe"})

    def test_post_api_empty_body(self):
        # Test POST /api/v1/sample-post-api with empty body
        response = self.app.post('/api/v1/sample-post-api', json={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "success", "message": "Received "}) 

if __name__ == '__main__':
    unittest.main()