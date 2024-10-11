# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for fn in self.array_transforms:
    arr = fn(arr)
    self.match(
        np_array_ops.all(arr, *args, **kwargs),
        np.all(arr, *args, **kwargs))
    self.match(
        np_array_ops.any(arr, *args, **kwargs),
        np.any(arr, *args, **kwargs))
