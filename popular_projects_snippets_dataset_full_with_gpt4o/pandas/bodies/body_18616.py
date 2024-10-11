# Extracted from ./data/repos/pandas/pandas/tests/libs/test_lib.py
target = np.arange(100)

# slice
indices = np.array([], dtype=np.intp)
maybe_slice = lib.maybe_indices_to_slice(indices, len(target))

assert isinstance(maybe_slice, slice)
tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
