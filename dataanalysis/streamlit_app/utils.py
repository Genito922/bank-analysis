import requests
import pandas as pd

API_URL = "https://credit-risk-api.onrender.com"

def fetch_data(endpoint: str, params: dict = None):
    url = f"{API_URL}{endpoint}"
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        return pd.DataFrame(resp.json())
    else:
        return pd.DataFrame()
