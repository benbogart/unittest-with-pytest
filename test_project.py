import pandas as pd

def test_add():
    import project
    assert project.add(1,1) == 2
    assert project.add(-1,-1) == -2

# def add_col(df, colname, coldata):
    
#     # add a column to a DataFrame
#     df[colname] = coldata
#     return df