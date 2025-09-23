import kagglehub
import pandas as pd
import os 
# Download latest version
path = kagglehub.dataset_download("altruistdelhite04/gold-price-data")

print("Path to dataset files:", path)
def load_data():
    return pd.read_csv(os.path.join(path ,'gld_price_data.csv'))
