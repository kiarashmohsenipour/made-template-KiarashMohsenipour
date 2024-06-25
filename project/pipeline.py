import io
import os
import sqlite3
import pandas as pd
import requests
import matplotlib.pyplot as plt
from kaggle.api.kaggle_api_extended import KaggleApi

try:
    # Define paths
    # data_path = './data'
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

    temperature_data = pd.read_csv(os.path.join(data_path, csv_files[0]))
    inflation_data = pd.read_csv(os.path.join(data_path, csv_files[1]))

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
