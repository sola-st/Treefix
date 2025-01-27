# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_function.py
a = pd.array(
    [True, True, False, False, True, None, True, None, False], dtype="boolean"
)
result = pd.core.algorithms.diff(a, 1)
expected = pd.array(
    [None, False, True, False, True, None, None, None, None], dtype="boolean"
)
tm.assert_extension_array_equal(result, expected)

ser = pd.Series(a)
result = ser.diff()
expected = pd.Series(expected)
tm.assert_series_equal(result, expected)
