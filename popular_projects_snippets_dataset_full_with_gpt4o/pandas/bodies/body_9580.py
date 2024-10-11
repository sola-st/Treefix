# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_astype.py
# with missing values
arr = pd.array([0.1, 0.2, None], dtype="Float64")

with pytest.raises(ValueError, match="cannot convert NA to integer"):
    arr.astype("int64")

with pytest.raises(ValueError, match="cannot convert float NaN to bool"):
    arr.astype("bool")

result = arr.astype("float64")
expected = np.array([0.1, 0.2, np.nan], dtype="float64")
tm.assert_numpy_array_equal(result, expected)

# no missing values
arr = pd.array([0.0, 1.0, 0.5], dtype="Float64")
result = arr.astype("int64")
expected = np.array([0, 1, 0], dtype="int64")
tm.assert_numpy_array_equal(result, expected)

result = arr.astype("bool")
expected = np.array([False, True, True], dtype="bool")
tm.assert_numpy_array_equal(result, expected)
