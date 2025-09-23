import kagglehub
import pandas as pd 
import os
from sklearn.model_selection import train_test_split
def load_data():
    path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
    data_path= os.path.join(path , 'creditcard.csv')
    return pd.read_csv(data_path)

def splited_data_unblanced():
    df=load_data()
    fruad_data=df[df.Class == 0]
    legit= df[df.Class == 1 ]
    legit_sampled = legit.sample(n=492)
    data= pd.concat([legit_sampled , fruad_data])
    X=data.drop(columns=['Class'])
    y=data['Class']
    
    X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=.1 , stratify=y , random_state=2)
    return X_train , X_test , y_train , y_test