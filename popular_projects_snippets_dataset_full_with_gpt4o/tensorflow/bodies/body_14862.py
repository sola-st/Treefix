# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
for fn in self.array_transforms:
    arg = fn(arr)
    self.match(
        np_math_ops.ptp(arg, *args, **kwargs), np.ptp(arg, *args, **kwargs))
