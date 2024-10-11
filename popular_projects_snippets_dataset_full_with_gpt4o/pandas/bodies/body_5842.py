# Extracted from ./data/repos/pandas/pandas/tests/extension/test_common.py
arr = DummyArray(np.array([1, 2, 3], dtype=np.int64))
result = arr.astype(arr.dtype, copy=False)

assert arr is result

result = arr.astype(arr.dtype)
assert arr is not result
