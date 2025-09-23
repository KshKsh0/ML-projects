import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.model_selection import train_test_split

data=sklearn.datasets.fetch_california_housing()
df=pd.DataFrame(data.data , columns=data.feature_names)
df['price']=data.target
def spillted_data_full():
    X=df.drop(columns=['price'])
    y=df['price']
    X_trian ,X_test , y_train ,y_test =train_test_split(X ,y ,test_size=.1 ,random_state=2)
    return X_trian ,X_test , y_train ,y_test  

print(spillted_data_full)
    
def spliting_based_on_corroleation():
    
    X=df.drop(columns=['price' , 'AveBedrms' ,'Population' , 'AveOccup' , 'Longitude'])
    y=df['price']
    
    X_trian ,X_test , y_train ,y_test =train_test_split(X ,y ,test_size=.1 ,random_state=2)
    return X_trian ,X_test , y_train ,y_test  
    