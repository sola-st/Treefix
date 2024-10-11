# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# Check that we parse strs in both scalar and listlike

# Setting list-like of strs
expected = arr1d.copy()
expected[[0, 1]] = arr1d[-2:]

result = arr1d.copy()
result[:2] = [str(x) for x in arr1d[-2:]]
tm.assert_equal(result, expected)

# Same thing but now for just a scalar str
expected = arr1d.copy()
expected[0] = arr1d[-1]

result = arr1d.copy()
result[0] = str(arr1d[-1])
tm.assert_equal(result, expected)
