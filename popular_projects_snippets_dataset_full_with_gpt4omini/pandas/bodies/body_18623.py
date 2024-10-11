# Extracted from ./data/repos/pandas/pandas/tests/libs/test_lib.py
# not slice
target = np.arange(10)
indices = np.array(case, dtype=np.intp)
maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
assert not isinstance(maybe_slice, slice)
tm.assert_numpy_array_equal(maybe_slice, indices)
tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
