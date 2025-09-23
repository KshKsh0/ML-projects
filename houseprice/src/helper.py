import  matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

def correlation_matrix(data:pd):
    cm=data.corr()
    plt.figure(figsize=(10,10))
    sns.heatmap(cm , cbar=True , square=True , fmt='.1f' , annot=True , annot_kws={'size':8} , cmap='Blues')
    