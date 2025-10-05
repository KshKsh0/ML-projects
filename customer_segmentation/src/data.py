import kagglehub
import os
# Download latest version
def load_data():
    path = kagglehub.dataset_download("vjchoudhary7/customer-segmentation-tutorial-in-python")
    data_path=os.path.join(path  , 'Mall_Customers.csv')
    return data_path