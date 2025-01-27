# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_values.py
# GH41634
ser = Series([23, 7, 21])
expected = np.sort(ser.values)

sorted_ser = ser.sort_values(ascending=ascending)
if not ascending:
    expected = expected[::-1]

result = sorted_ser.values
tm.assert_numpy_array_equal(result, expected)
