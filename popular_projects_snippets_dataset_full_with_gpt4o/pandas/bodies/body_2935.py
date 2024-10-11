# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dtypes.py
# GH6525
df = DataFrame(index=range(5), columns=list("abc"), dtype=np.float_)
tm.assert_series_equal(
    df.dtypes,
    Series({"a": np.float_, "b": np.float_, "c": np.float_}),
)
tm.assert_series_equal(df.iloc[:, 2:].dtypes, Series({"c": np.float_}))
tm.assert_series_equal(
    df.dtypes,
    Series({"a": np.float_, "b": np.float_, "c": np.float_}),
)
