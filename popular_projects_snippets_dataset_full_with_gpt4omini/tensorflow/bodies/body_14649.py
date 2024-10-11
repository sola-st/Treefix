# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for fn1 in self.array_transforms:
    for fn2 in self.array_transforms:
        arr_arg = fn1(arr)
        axes_arg = fn2(axes) if axes is not None else None
        self.match(
            np_array_ops.transpose(arr_arg, axes_arg),
            np.transpose(arr_arg, axes))
