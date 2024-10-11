# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for fn1 in self.array_transforms:
    for fn2 in self.array_transforms:
        arg1 = fn1(condition)
        arg2 = fn2(arr)
        self.match(
            np_array_ops.compress(arg1, arg2, *args, **kwargs),
            np.compress(
                np.asarray(arg1).astype(np.bool_), arg2, *args, **kwargs))
