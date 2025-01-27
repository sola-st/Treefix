# Extracted from ./data/repos/pandas/pandas/tests/frame/conftest.py
"""
    Fixture for DataFrame of booleans with index of unique strings

    Columns are ['A', 'B', 'C', 'D']; some entries are missing

                    A      B      C      D
    zBZxY2IDGd  False  False  False  False
    IhBWBMWllt  False   True   True   True
    ctjdvZSR6R   True  False   True   True
    AVTujptmxb  False   True  False   True
    G9lrImrSWq  False  False  False   True
    sFFwdIUfz2    NaN    NaN    NaN    NaN
    s15ptEJnRb    NaN    NaN    NaN    NaN
    ...           ...    ...    ...    ...
    UW41KkDyZ4   True   True  False  False
    l9l6XkOdqV   True  False  False  False
    X2MeZfzDYA  False   True  False  False
    xWkIKU7vfX  False   True  False   True
    QOhL6VmpGU  False  False  False   True
    22PwkRJdat  False   True  False  False
    kfboQ3VeIK   True  False   True  False

    [30 rows x 4 columns]
    """
df = DataFrame(tm.getSeriesData()) > 0
df = df.astype(object)
# set some NAs
df.iloc[5:10] = np.nan
df.iloc[15:20, -2:] = np.nan

# For `any` tests we need to have at least one True before the first NaN
#  in each column
for i in range(4):
    df.iloc[i, i] = True
exit(df)
