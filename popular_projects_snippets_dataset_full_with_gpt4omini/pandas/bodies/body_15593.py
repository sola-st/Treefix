# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#26215
data = ["a", np.nan, "b", np.nan, np.nan]
ser = Series(Categorical(data, categories=["a", "b", "c", "d", "e"]))
exp = Series(Categorical(expected_output, categories=["a", "b", "c", "d", "e"]))
result = ser.fillna(fill_value)
tm.assert_series_equal(result, exp)
