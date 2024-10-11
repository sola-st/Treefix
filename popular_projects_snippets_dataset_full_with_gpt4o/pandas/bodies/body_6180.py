# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
b, c, a = data_for_sorting
arr = data_for_sorting.take([2, 0, 1])  # to get [a, b, c]

if as_series:
    arr = pd.Series(arr)
assert arr.searchsorted(a) == 0
assert arr.searchsorted(a, side="right") == 1

assert arr.searchsorted(b) == 1
assert arr.searchsorted(b, side="right") == 2

assert arr.searchsorted(c) == 2
assert arr.searchsorted(c, side="right") == 3

result = arr.searchsorted(arr.take([0, 2]))
expected = np.array([0, 2], dtype=np.intp)

tm.assert_numpy_array_equal(result, expected)

# sorter
sorter = np.array([1, 2, 0])
assert data_for_sorting.searchsorted(a, sorter=sorter) == 0
