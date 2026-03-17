import unittest
from app import app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config["TESTING"] = True

        self.client = self.app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["status"], "healthy")

    def test_api_data_endpoint(self):
        response = self.client.get("/api/data")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("message", data)
        self.assertIn("items", data)
        self.assertIsInstance(data["items"], list)


if __name__ == "__main__":
    unittest.main()
