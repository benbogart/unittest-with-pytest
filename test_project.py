import pytest
import pandas as pd
import project


def test_add():
    import project

    # test basic functionality
    assert project.add(1,1) == 2

    # try a border case
    assert project.add(-1,-1) == -2


@pytest.mark.parametrize("a,b,expected", [[2,1,1], [-1,1,-2]])
def test_subtract(a, b, expected):

     assert project.subtract(a,b) == expected


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

    assert project.add_col(df, 'n_ears', 2).equals(df_expected)
