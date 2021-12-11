import pandas as pd

def clean_df(df):
    # drop unnamed columns
    df.drop(df.columns[df.columns.str.contains('unnamed', case = False)],axis=1, inplace=True)
    ## replace commna with dot for future float computations
    ## rename column(s) 
    new_names = {'Age_of_woman': 'Age', 'Induced_abortions': 'Induced abortions'}
    df.rename(columns = new_names, inplace = True)
    return df

