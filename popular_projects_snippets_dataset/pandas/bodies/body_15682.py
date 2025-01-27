# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# #1698
index = date_range("1/1/2012", periods=4, freq="12D")
ts = Series([0, 12, 24, 36], index)
new_index = index.append(index + pd.DateOffset(days=1)).sort_values()

exp = ts.reindex(new_index).interpolate(method="time")

index = date_range("1/1/2012", periods=4, freq="12H")
ts = Series([0, 12, 24, 36], index)
new_index = index.append(index + pd.DateOffset(hours=1)).sort_values()
result = ts.reindex(new_index).interpolate(method="time")

tm.assert_numpy_array_equal(result.values, exp.values)
