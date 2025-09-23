import kagglehub
import os
import pandas as pd 
def load_data():
    path = kagglehub.dataset_download("uciml/red-wine-quality-cortez-et-al-2009")
    csv_path = os.path.join(path, "winequality-red.csv")
    return pd.read_csv(csv_path)

