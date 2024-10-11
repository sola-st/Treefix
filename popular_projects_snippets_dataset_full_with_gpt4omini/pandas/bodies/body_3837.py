# Extracted from ./data/repos/pandas/pandas/tests/frame/conftest.py
"""
    Fixture for DataFrame of floats with index of unique strings

    Columns are ['A', 'B', 'C', 'D']; some entries are missing

                       A         B         C         D
    ABwBzA0ljw -1.128865 -0.897161  0.046603  0.274997
    DJiRzmbyQF  0.728869  0.233502  0.722431 -0.890872
    neMgPD5UBF  0.486072 -1.027393 -0.031553  1.449522
    0yWA4n8VeX -1.937191 -1.142531  0.805215 -0.462018
    3slYUbbqU1  0.153260  1.164691  1.489795 -0.545826
    soujjZ0A08       NaN       NaN       NaN       NaN
    7W6NLGsjB9       NaN       NaN       NaN       NaN
    ...              ...       ...       ...       ...
    uhfeaNkCR1 -0.231210 -0.340472  0.244717 -0.901590
    n6p7GYuBIV -0.419052  1.922721 -0.125361 -0.727717
    ZhzAeY6p1y  1.234374 -1.425359 -0.827038 -0.633189
    uWdPsORyUh  0.046738 -0.980445 -1.102965  0.605503
    3DJA6aN590 -0.091018 -1.684734 -1.100900  0.215947
    2GBPAzdbMk -2.883405 -1.021071  1.209877  1.633083
    sHadBoyVHw -2.223032 -0.326384  0.258931  0.245517

    [30 rows x 4 columns]
    """
df = DataFrame(tm.getSeriesData())
# set some NAs
df.iloc[5:10] = np.nan
df.iloc[15:20, -2:] = np.nan
exit(df)
