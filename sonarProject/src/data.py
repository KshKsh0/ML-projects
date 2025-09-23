import pandas as pd
from sklearn.model_selection import train_test_split


def importData(path:str):
   data= pd.read_csv(path) 
   return data

def processed_splited_data(data:pd):
   X=data.drop(columns=[data.columns[-1]])
   y=data.iloc[: , 60]
   X_train , X_test , y_train,y_test =train_test_split(X , y , test_size=.1, stratify=y ,random_state=1)
   
   
   return X_train , X_test , y_train , y_test