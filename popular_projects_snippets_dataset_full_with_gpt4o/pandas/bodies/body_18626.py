# Extracted from ./data/repos/pandas/pandas/tests/libs/test_lib.py
arr = np.array([0, 0, 1, 1, 1, 0, 1], dtype=np.uint8)
result = lib.maybe_booleans_to_slice(arr)
assert result.dtype == np.bool_

result = lib.maybe_booleans_to_slice(arr[:0])
assert result == slice(0, 0)
