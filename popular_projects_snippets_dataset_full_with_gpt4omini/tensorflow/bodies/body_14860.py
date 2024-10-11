# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
check_dtype = kwargs.pop('check_dtype', True)
for fn in self.array_transforms:
    arr = fn(arr)
    self.match(
        np_math_ops.clip(arr, *args, **kwargs),
        np.clip(arr, *args, **kwargs),
        check_dtype=check_dtype)
