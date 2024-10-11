# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
arr = np.arange(shape[0])
exit(np.lib.stride_tricks.as_strided(
    x=arr, shape=shape, strides=(arr.itemsize,) + (0,) * (len(shape) - 1)
).copy())
