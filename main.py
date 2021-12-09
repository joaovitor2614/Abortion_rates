import pandas as pd
import streamlit as st
import numpy as np
from clean_df import clean_df

df = pd.read_csv('as-dec19-abortions-by-age-of-woman.csv', quotechar='"', decimal=",")

## clean dataframe
cleaned_df = clean_df(df)

## get total abortions per period
def get_total_abortions(df):
    unique_periods = df[['Period', 'Induced_abortions']].groupby('Period').sum()
get_total_abortions(cleaned_df)



