import os
import unittest
import pandas as pd
from pipeline import temperature_data, inflation_data

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
output_file = os.path.join(data_path, 'merged_data.csv')

class TestProject5(unittest.TestCase):

    def setUp(self):
        self.temperature = temperature_data
        self.inflation = inflation_data

    def test_data_path_exists(self):
        self.assertTrue(os.path.exists(data_path), "Data path does not exist.")

    def test_data_path_is_not_empty(self):
        self.assertTrue(os.listdir(data_path), "Data path is empty.")

    def test_temperature_data_has_rows(self):
        self.assertGreater(self.temperature.shape[0], 0, "Weather data should have rows")

    def test_inflation_data_has_rows(self):
        self.assertGreater(self.inflation.shape[0], 0, "Inflation data should have rows")


if __name__ == '__main__':
    unittest.main()
