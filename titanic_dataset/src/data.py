import pandas as pd

def load_data_preprocessed(df:pd):
    df=df.drop(columns=['Cabin', 'PassengerId' , 'Name' , 'Ticket'])
    df['Age'].fillna(df['Age'].mean(),inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0],inplace=True)
    df.replace({'Sex' : {'male' : 0  , 'female' : 1 } , 'Embarked': {'S' : 0 , "C" : 1  , 'Q' : 2}} , inplace = True)
    return df
