import pandas as pd


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_col(df, colname, coldata):
    
    # add a column to a DataFrame
    df[colname] = coldata
    return df