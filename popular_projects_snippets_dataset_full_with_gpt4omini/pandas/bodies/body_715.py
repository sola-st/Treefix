# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
func = getattr(lib, func)
arr = np.array(["foo", "bar"])
assert not func(arr)
assert not func(arr.reshape(2, 1))

arr = np.array([1, 2])
assert not func(arr)
assert not func(arr.reshape(2, 1))
