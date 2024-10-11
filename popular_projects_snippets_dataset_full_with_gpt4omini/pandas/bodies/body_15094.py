# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
index = pd.MultiIndex.from_tuples(multiindex)
series = Series(data, index=index)
result = series.to_numpy(dtype=dtype, na_value=na_value)
expected = np.array(expected)
tm.assert_numpy_array_equal(result, expected)
