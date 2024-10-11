# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#17033
# Test fillna for a Categorical series
data = ["a", np.nan, "b", np.nan, np.nan]
ser = Series(Categorical(data, categories=["a", "b"]))
exp = Series(Categorical(expected_output, categories=["a", "b"]))
result = ser.fillna(fill_value)
tm.assert_series_equal(result, exp)
