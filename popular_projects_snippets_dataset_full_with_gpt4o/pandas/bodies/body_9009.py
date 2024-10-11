# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
arr = SparseArray([0, 1, 2])
expected = SparseArray([10, 11, 12], fill_value=10)

# dict
result = arr.map({0: 10, 1: 11, 2: 12})
tm.assert_sp_array_equal(result, expected)

# series
result = arr.map(pd.Series({0: 10, 1: 11, 2: 12}))
tm.assert_sp_array_equal(result, expected)

# function
result = arr.map(pd.Series({0: 10, 1: 11, 2: 12}))
expected = SparseArray([10, 11, 12], fill_value=10)
tm.assert_sp_array_equal(result, expected)
