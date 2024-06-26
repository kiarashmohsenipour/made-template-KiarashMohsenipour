import io
import os
import sqlite3
import pandas as pd
import requests
import matplotlib.pyplot as plt
from kaggle.api.kaggle_api_extended import KaggleApi

try:
    # Define paths
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    db_name = 'temperature_inflation.db'
    # Kaggle dataset identifiers
    URL_1 = "adamwurdits/finland-norway-and-sweden-weather-data-20152019"
    URL_2 = "sazidthe1/global-inflation-data"
    # Download datasets from Kaggle
    api = KaggleApi()
    api.authenticate()


    api.dataset_download_files(URL_1, path=data_path, unzip=True)
    api.dataset_download_files(URL_2, path=data_path, unzip=True)

    csv_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]

    inflation_data = pd.read_csv(os.path.join(data_path, csv_files[0]))
    temperature_data = pd.read_csv(os.path.join(data_path, csv_files[1]))

    # print(temperature_data.columns)
    # print(inflation_data.columns)

    temperature_data['date'] = pd.to_datetime(temperature_data['date'], format='%m/%d/%Y')
    temperature_data['date'] = temperature_data['date'].dt.year


    # Reshape inflation data
    inflation_data_melted = inflation_data.melt(id_vars=["country_name", "indicator_name"],
                                                var_name="year",
                                                value_name="inflation_rate")
    # Filter for the years 2015-2019
    inflation_data_filtered = inflation_data_melted[inflation_data_melted['year'].astype(int).between(2015, 2019)]

    # Merge the datasets on country and year
    temperature_data['country'] = temperature_data['country'].str.strip()  # Remove any leading/trailing spaces

    # inflation_data_filtered['country_name'] = inflation_data_filtered[
    #     'country_name'].str.strip()  # Remove any leading/trailing spaces

    # # Rename columns for consistency
    # temperature_data.rename(columns={'country': 'country_name'}, inplace=True)
    # temperature_data.rename(columns={'date': 'year'}, inplace=True)

    # # Convert year columns to integer
    temperature_data['date'] = temperature_data['date'].astype(int)
    inflation_data_filtered.loc[:, 'year'] = inflation_data_filtered['year'].astype(int)

    # Merge datasets
    merged_data = pd.merge(temperature_data, inflation_data_filtered,
                           how='inner',
                           left_on=['country', 'date'],
                           right_on=['country_name', 'year'])

    # print(merged_data.columns)

    merged_csv_path = os.path.join(data_path, 'merged_data.csv')

    path = os.path.join(data_path, 'temperature_inflation.db')
    conn = sqlite3.connect(path)

    temperature_data.to_sql('temperature_data', conn, if_exists='replace', index=False)

    # Insert data into the inflation_data table
    inflation_data.to_sql('inflation_data', conn, if_exists='replace', index=False)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
except Exception as e:
    print(f"error: {e}")
