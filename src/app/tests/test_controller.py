"""

Tests for Controllers

"""
import unittest
import logging
from fastapi.testclient import TestClient
from app.main import app

########## Testing the App ###############


class TestUserPartController(unittest.TestCase):
    """

    unit test for  api_controller

    """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def teardown_class(cls):
        """
        Shutdown after Finishing all Tests

        """
        logging.shutdown()

    def setUp(self):
        self.client = TestClient(app)

    def test_get_info(self):
        """
        test to check if info page works

        """
        response = self.client.get("/info")

        msg = {
            "app_name": "Currency Converter API Services",
            "env_name": "Scraping Services",
            "version": 2,
            "description": "Currency Converter Converts Currency"
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), msg)
        self.assertIsInstance(response.json(), dict)
