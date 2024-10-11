# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_numpy.py
arr = np.random.randn(4, 3)
df = DataFrame(arr)
assert df.values.base is arr
assert df.to_numpy(copy=False).base is arr
assert df.to_numpy(copy=True).base is not arr
