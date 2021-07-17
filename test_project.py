import pytest
import pandas as pd


def test_add():
    import project

    # test basic functionality
    assert project.add(1,1) == 2

    # try a border case
    assert project.add(-1,-1) == -2


def test_add_col():
     import project

     # start
     df = pd.DataFrame([[0, 1], [2, 3]],
                      index=['cat', 'dog'],
                      columns=['weight', 'height'])

     # expected
     df_expected = pd.DataFrame([[0, 1, 2], [2, 3, 2]],
                               index=['cat', 'dog'],
                               columns=['weight', 'height', 'n_ears'])

     # test the result
     assert project.add_col(df, 'n_ears', 2).equals(df_expected)

# test parameterization
@pytest.mark.parametrize("a,b,expected", [[2,1,1], [-1,1,-2]])
def test_subtract(a, b, expected):
     import project

     assert project.subtract(a,b) == expected


# fixtures
@pytest.fixture()
def df():
     df = pd.DataFrame([[0, 1], [2, 3]],
                       index=['wallaby', 'kangaroo'],
                       columns=['weight', 'height'])

     return df


def test_add_col2(df):
     import project

     # expected
     df_expected = pd.DataFrame([[0, 1, 3], [2, 3, 5]],
                               index=['wallaby', 'kangaroo'],
                               columns=['weight', 'height', 'hop_height'])

     assert project.add_col(df, 'hop_height', [3,5]).equals(df_expected)



