# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, *args, **kwargs):
    axis = kwargs.pop('axis', None)
    for fn1 in self.array_transforms:
        for fn2 in self.array_transforms:
            arr_arg = fn1(arr)
            axis_arg = fn2(axis) if axis is not None else None
            self.match(
                np_array_ops.var(arr_arg, axis=axis_arg, *args, **kwargs),
                np.var(arr_arg, axis=axis, *args, **kwargs))

run_test([1, 2, 1])
run_test([1., 2., 1.])
run_test([1.j, 2., 1.j])
run_test([1., 2., 1.], dtype=np.int64)
run_test([[1, 2], [3, 4]], axis=1)
run_test([[1, 2], [3, 4]], axis=0)
run_test([[1, 2], [3, 4]], axis=-1)
run_test([[1, 2], [3, 4]], axis=-2)
run_test([[1, 2], [3, 4]], axis=(0, 1))
run_test(np.arange(8).reshape((2, 2, 2)).tolist(), axis=(0, 2))
run_test(
    np.arange(8).reshape((2, 2, 2)).tolist(), axis=(0, 2), keepdims=True)
run_test(np.arange(8).reshape((2, 2, 2)).tolist(), axis=(2, 0))
run_test(
    np.arange(8).reshape((2, 2, 2)).tolist(), axis=(2, 0), keepdims=True)
self.assertRaises(ValueError, np_array_ops.var, np.ones([2, 2]), out=[])
