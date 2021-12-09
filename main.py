import pandas as pd
import streamlit as st
import numpy as np
from clean_df import clean_df

df = pd.read_csv('as-dec19-abortions-by-age-of-woman.csv', quotechar='"', decimal=",")

## clean dataframe
cleaned_df = clean_df(df)

## get total abortions per period
def get_total_abortions(df):
    unique_periods = sorted(df.Period.unique())
    ##new_values = df.loc[df['Period'] == 2000]
    for i in range(len(unique_periods)):
        total_sum = 0
        period_values = df.loc[df['Period'] == unique_periods[i]]
        print(period_values)
        period_abortions = period_values['Induced_abortions'].tolist()
        
        for i in range(len(period_abortions)):
            current_value = period_abortions[i]
            total_sum += int(current_value)
        ##print(f'Total abortions in {unique_periods[i]} is {total_sum}')

       

       
     

    

get_total_abortions(cleaned_df)



