# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
arr = data[:5].copy()
expected = data.take([0, 0, 0, 3, 4])

if box_in_series:
    arr = pd.Series(arr)
    expected = pd.Series(expected)

arr[idx] = arr[0]
self.assert_equal(arr, expected)
