# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
# GH-44499
arr = pd.array([True, False])
result = arr == other
expected = pd.array([False, False])
tm.assert_extension_array_equal(result, expected)

result = arr != other
expected = pd.array([True, True])
tm.assert_extension_array_equal(result, expected)
