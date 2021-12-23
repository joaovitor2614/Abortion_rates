import pandas as pd
import streamlit as st
import numpy as np
from clean_df import clean_df

df = pd.read_csv('as-dec19-abortions-by-age-of-woman.csv', quotechar='"', decimal=",")

## clean dataframe
cleaned_df = clean_df(df)

## get total abortions per period and
def get_total_abortions(df):
    unique_periods = df[['Period', 'Induced abortions']].groupby('Period').sum()


    return unique_periods

st.markdown("""
# Total de abortos induzidos por ano  /   Porcentagem de abortos induzidos em um período de 19 anos

""")
period_total = get_total_abortions(cleaned_df)
st.bar_chart(period_total, width=650)


## get percentage of induced abortions per year based on total
def get_percentage(period_total):
    absolut_total = period_total['Induced abortions'].sum()
    divided_df = period_total['Induced abortions'].divide(absolut_total)
    percentage_per_year = divided_df.multiply(100)
    percentage_per_year_around = np.around(percentage_per_year, decimals=1)

    return percentage_per_year_around


percentage_per_year = get_percentage(period_total)

percentage_per_year_todf = percentage_per_year.to_frame('Percentage')
percentage_per_year_todf.index.name = 'Year'
st.markdown("""

Percentage of induced abortions across 19 years range
""")
st.dataframe(percentage_per_year_todf, width=450)



