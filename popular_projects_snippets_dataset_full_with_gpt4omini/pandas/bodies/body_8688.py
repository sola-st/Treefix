# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
other = pd.Categorical(arr1d, ordered=ordered)
if as_index:
    other = pd.CategoricalIndex(other)

left, right = arr1d, other
if reverse:
    left, right = right, left

ones = np.ones(arr1d.shape, dtype=bool)
zeros = ~ones

result = left == right
tm.assert_numpy_array_equal(result, ones)

result = left != right
tm.assert_numpy_array_equal(result, zeros)

if not reverse and not as_index:
    # Otherwise Categorical raises TypeError bc it is not ordered
    # TODO: we should probably get the same behavior regardless?
    result = left < right
    tm.assert_numpy_array_equal(result, zeros)

    result = left <= right
    tm.assert_numpy_array_equal(result, ones)

    result = left > right
    tm.assert_numpy_array_equal(result, zeros)

    result = left >= right
    tm.assert_numpy_array_equal(result, ones)
