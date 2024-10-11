# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for fn in self.array_transforms:
    arg = fn(arr)
    self.match(
        np_array_ops.cumprod(arg, *args, **kwargs),
        np.cumprod(arg, *args, **kwargs))
    self.match(
        np_array_ops.cumsum(arg, *args, **kwargs),
        np.cumsum(arg, *args, **kwargs))
