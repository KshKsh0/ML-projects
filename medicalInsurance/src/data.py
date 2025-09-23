import kagglehub
import os 
import pandas as pd 
def load_data():
    path = kagglehub.dataset_download("mirichoi0218/insurance")
    data_path = os.path.join(path , 'insurance.csv')
    return pd.read_csv(data_path)