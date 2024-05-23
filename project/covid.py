import io
import os
import sqlite3
import pandas as pd
import requests

dataset_url_link = "https://covidtracking.com/data/download/all-states-history.csv"
os.makedirs("../data", exist_ok=True)

try:
    s = requests.get(dataset_url_link).content.decode("utf8")
    df = pd.read_csv(io.StringIO(s))
    #        db_path = os.path.join(data_directory, "covid.db")
    os.makedirs(os.path.dirname("../data/covid.db"), exist_ok=True)
    conn = sqlite3.connect("../data/covid.db")
    df.to_sql("covid", conn, if_exists="replace", index=False)
    conn.close()
except Exception as e:
    print(f"error: {e}")
