# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_to_numpy.py
con = pd.Series if box else pd.array

# no missing values -> can convert to float, otherwise raises
arr = con([0.1, 0.2, 0.3], dtype="Float64")
result = arr.to_numpy(dtype="float64")
expected = np.array([0.1, 0.2, 0.3], dtype="float64")
tm.assert_numpy_array_equal(result, expected)

arr = con([0.1, 0.2, None], dtype="Float64")
with pytest.raises(ValueError, match="cannot convert to 'float64'-dtype"):
    result = arr.to_numpy(dtype="float64")

# need to explicitly specify na_value
result = arr.to_numpy(dtype="float64", na_value=np.nan)
expected = np.array([0.1, 0.2, np.nan], dtype="float64")
tm.assert_numpy_array_equal(result, expected)
