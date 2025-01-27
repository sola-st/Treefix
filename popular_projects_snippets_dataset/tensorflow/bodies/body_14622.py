# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
axis = kwargs.pop('axis', None)
for fn1 in self.array_transforms:
    for fn2 in self.array_transforms:
        arr_arg = fn1(arr)
        axis_arg = fn2(axis) if axis is not None else None
        self.match(
            np_array_ops.std(arr_arg, axis=axis_arg, *args, **kwargs),
            np.std(arr_arg, axis=axis, *args, **kwargs))
