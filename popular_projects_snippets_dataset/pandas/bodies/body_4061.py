# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
df = DataFrame({"A": [1, 1, 1], "B": [1, 2, 3], "C": [1, np.nan, 3]})
tm.assert_series_equal(df.nunique(), Series({"A": 1, "B": 3, "C": 2}))
tm.assert_series_equal(
    df.nunique(dropna=False), Series({"A": 1, "B": 3, "C": 3})
)
tm.assert_series_equal(df.nunique(axis=1), Series({0: 1, 1: 2, 2: 2}))
tm.assert_series_equal(
    df.nunique(axis=1, dropna=False), Series({0: 1, 1: 3, 2: 2})
)
