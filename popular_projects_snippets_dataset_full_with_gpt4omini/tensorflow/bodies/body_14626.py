# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for fn in self.array_transforms:
    arg = fn(arr)
    self.match(
        np_array_ops.prod(arg, *args, **kwargs),
        np.prod(arg, *args, **kwargs))
