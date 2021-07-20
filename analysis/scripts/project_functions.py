import numpy as np
#import pandas
import pandas as pd

def load_and_process(url_or_path_to_csv_file):


    df = (   
         pd.read_csv(url_or_path_to_csv_file) 
        .rename(columns={"bmi": "bmi (Body Mass Index)"})
        .rename(columns={"region": "USA Region"})
        .loc[lambda x: x['age']>17]
        .sort_values("age", ascending=True)    
        )

    return df