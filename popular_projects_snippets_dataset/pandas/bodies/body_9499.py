# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_construction.py
con = pd.Series if box else pd.array
# default (with or without missing values) -> object dtype
arr = con([True, False, True], dtype="boolean")
result = arr.to_numpy()
expected = np.array([True, False, True], dtype="object")
tm.assert_numpy_array_equal(result, expected)

arr = con([True, False, None], dtype="boolean")
result = arr.to_numpy()
expected = np.array([True, False, pd.NA], dtype="object")
tm.assert_numpy_array_equal(result, expected)

arr = con([True, False, None], dtype="boolean")
result = arr.to_numpy(dtype="str")
expected = np.array([True, False, pd.NA], dtype=f"{tm.ENDIAN}U5")
tm.assert_numpy_array_equal(result, expected)

# no missing values -> can convert to bool, otherwise raises
arr = con([True, False, True], dtype="boolean")
result = arr.to_numpy(dtype="bool")
expected = np.array([True, False, True], dtype="bool")
tm.assert_numpy_array_equal(result, expected)

arr = con([True, False, None], dtype="boolean")
with pytest.raises(ValueError, match="cannot convert to 'bool'-dtype"):
    result = arr.to_numpy(dtype="bool")

# specify dtype and na_value
arr = con([True, False, None], dtype="boolean")
result = arr.to_numpy(dtype=object, na_value=None)
expected = np.array([True, False, None], dtype="object")
tm.assert_numpy_array_equal(result, expected)

result = arr.to_numpy(dtype=bool, na_value=False)
expected = np.array([True, False, False], dtype="bool")
tm.assert_numpy_array_equal(result, expected)

result = arr.to_numpy(dtype="int64", na_value=-99)
expected = np.array([1, 0, -99], dtype="int64")
tm.assert_numpy_array_equal(result, expected)

result = arr.to_numpy(dtype="float64", na_value=np.nan)
expected = np.array([1, 0, np.nan], dtype="float64")
tm.assert_numpy_array_equal(result, expected)

# converting to int or float without specifying na_value raises
with pytest.raises(ValueError, match="cannot convert to 'int64'-dtype"):
    arr.to_numpy(dtype="int64")
with pytest.raises(ValueError, match="cannot convert to 'float64'-dtype"):
    arr.to_numpy(dtype="float64")
