"""

Tests for Controllers

"""
import os


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

    def test_get_base(self):
        """
        test to check if base page works

        """
        response = self.client.get("/")

        msg = {"Stylight": "Currency Converter Service"}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), msg)
        self.assertIsInstance(response.json(), dict)

    def test_get_valid_conversion(self):
        """
        test to check if base page works

        """
        response = self.client.get(
            "/convert/?input_value=1&input_currency=USD&output_currency=EUR")

        msg = {"value": 0.913, "currency": "EUR"}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), msg)
        self.assertIsInstance(response.json(), dict)

    def test_get_invalid_input(self):
        """
        test for invalid input currency

        """
        response = self.client.get(
            "/convert/?input_value=1&input_currency=KKK&output_currency=USD")

        msg = {"value": 1, "currency": "input currency not supported"}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), msg)
        self.assertIsInstance(response.json(), dict)

    def test_get_invalid_output(self):
        """
        test for invalid output currency

        """
        response = self.client.get(
            "/convert/?input_value=1&input_currency=USD&output_currency=KKK")

        msg = {"value": 1, "currency": "output currency not supported"}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), msg)
        self.assertIsInstance(response.json(), dict)

    def test_get_invalid(self):
        """
        test for invalid inputs

        """
        response = self.client.get(
            "/convert/?input_value=1&input_currency=2&output_currency=3")

        msg = {"result": "Invalid Input"}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), msg)
        self.assertIsInstance(response.json(), dict)
