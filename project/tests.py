# import os.path
#
# from pipeline import *
#
#
# def test_project5():
#     data_path = './data'
#     output_file = os.path.join(data_path, 'merged_data.csv')
#
#     temperature = temperature_data
#     inflation = inflation_data
#
#     assert os.path.exists(data_path)
#     assert os.listdir(data_path)
#
#     assert os.path.exists(output_file), "Output file does not exist."
#
#     merged_data_loaded = pd.read_csv(output_file)
#     assert not merged_data_loaded.empty, "Merged data is empty."
#     assert 'country_name' in merged_data_loaded.columns, "Expected column 'country_name' not found in merged data."
#     assert 'inflation_rate' in merged_data_loaded.columns, "Expected column 'inflation_rate' not found in merged data."
#
#     expected_columns = ['country_name', 'year', 'inflation_rate']
#     for column in expected_columns:
#         assert column in merged_data_loaded.columns, f"Expected column '{column}' not found in merged data."
#
#     assert temperature.shape[0] > 0, "Weather data should have rows"
#     assert inflation.shape[0] > 0, "Inflation data should have rows"
#
#     duplicated_rows = merged_data_loaded.duplicated(subset=['country_name', 'date'], keep=False)
#     assert not duplicated_rows.any(), "Merged data should have no duplicate rows for the same country and year"
#
#     assert not merged_data_loaded[['country_name', 'year',
#                             'inflation_rate']].isnull().any().any(), "Merged data should have no missing values in critical columns"

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

    # def test_output_file_exists(self):
    #     self.assertTrue(os.path.exists(output_file), "Output file does not exist.")

    # def test_merged_data_not_empty(self):
    #     merged_data_loaded = pd.read_csv(output_file)
    #     self.assertFalse(merged_data_loaded.empty, "Merged data is empty.")

    # def test_merged_data_columns(self):
    #     merged_data_loaded = pd.read_csv(output_file)
    #     self.assertIn('country_name', merged_data_loaded.columns,
    #                   "Expected column 'country_name' not found in merged data.")
    #     self.assertIn('inflation_rate', merged_data_loaded.columns,
    #                   "Expected column 'inflation_rate' not found in merged data.")
    #     expected_columns = ['country_name', 'year', 'inflation_rate']
    #     for column in expected_columns:
    #         self.assertIn(column, merged_data_loaded.columns, f"Expected column '{column}' not found in merged data.")

    def test_temperature_data_has_rows(self):
        self.assertGreater(self.temperature.shape[0], 0, "Weather data should have rows")

    def test_inflation_data_has_rows(self):
        self.assertGreater(self.inflation.shape[0], 0, "Inflation data should have rows")

    # def test_no_missing_values_in_merged_data(self):
    #     merged_data_loaded = pd.read_csv(output_file)
    #     self.assertFalse(
    #         merged_data_loaded[['country_name', 'year', 'inflation_rate']].isnull().any().any(),
    #         "Merged data should have no missing values in critical columns"
    #     )



if __name__ == '__main__':
    unittest.main()
