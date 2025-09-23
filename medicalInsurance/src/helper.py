import pandas as pd

def data_processing(df:pd):
    df.replace({'sex' : {'male' :1 , 'female' : 0}} , inplace= True)
    df.replace({'smoker' : {'yes' : 1 , "no" : 0 }} , inplace = True)
    df.replace({'region' : { 'southeast' : 0, 'southwest' : 1   ,'northeast' : 2 , 'northwest' : 3  }} , inplace=True)    
    return df