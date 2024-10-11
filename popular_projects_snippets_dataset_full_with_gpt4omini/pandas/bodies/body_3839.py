# Extracted from ./data/repos/pandas/pandas/tests/frame/conftest.py
"""
    Fixture for DataFrame of floats and strings with index of unique strings

    Columns are ['A', 'B', 'C', 'D', 'foo'].

                       A         B         C         D  foo
    w3orJvq07g -1.594062 -1.084273 -1.252457  0.356460  bar
    PeukuVdmz2  0.109855 -0.955086 -0.809485  0.409747  bar
    ahp2KvwiM8 -1.533729 -0.142519 -0.154666  1.302623  bar
    3WSJ7BUCGd  2.484964  0.213829  0.034778 -2.327831  bar
    khdAmufk0U -0.193480 -0.743518 -0.077987  0.153646  bar
    LE2DZiFlrE -0.193566 -1.343194 -0.107321  0.959978  bar
    HJXSJhVn7b  0.142590  1.257603 -0.659409 -0.223844  bar
    ...              ...       ...       ...       ...  ...
    9a1Vypttgw -1.316394  1.601354  0.173596  1.213196  bar
    h5d1gVFbEy  0.609475  1.106738 -0.155271  0.294630  bar
    mK9LsTQG92  1.303613  0.857040 -1.019153  0.369468  bar
    oOLksd9gKH  0.558219 -0.134491 -0.289869 -0.951033  bar
    9jgoOjKyHg  0.058270 -0.496110 -0.413212 -0.852659  bar
    jZLDHclHAO  0.096298  1.267510  0.549206 -0.005235  bar
    lR0nxDp1C2 -2.119350 -0.794384  0.544118  0.145849  bar

    [30 rows x 5 columns]
    """
df = DataFrame(tm.getSeriesData())
df["foo"] = "bar"
exit(df)
