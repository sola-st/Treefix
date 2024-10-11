# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
missing_df = tm.makeDataFrame()
missing_df.loc[missing_df.index[0], "A"] = np.nan
with np.errstate(invalid="ignore"):
    expected = missing_df.values < 0
with np.errstate(invalid="raise"):
    result = (missing_df < 0).values
tm.assert_numpy_array_equal(result, expected)
