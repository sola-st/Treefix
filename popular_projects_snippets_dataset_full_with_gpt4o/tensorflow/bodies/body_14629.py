# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
axis_transforms = [
    lambda x: x,  # Identity,
    ops.convert_to_tensor,
    np.array,
    np_array_ops.array,
    lambda x: np_array_ops.array(x, dtype=np.float32),
    lambda x: np_array_ops.array(x, dtype=np.float64),
]

def run_test(a, **kwargs):
    axis = kwargs.pop('axis', None)
    for fn1 in self.array_transforms:
        for fn2 in axis_transforms:
            arg1 = fn1(a)
            axis_arg = fn2(axis) if axis is not None else None
            self.match(
                math_fun(arg1, axis=axis_arg, **kwargs),
                np_fun(arg1, axis=axis, **kwargs),
                msg='{}({}, axis={}, keepdims={})'.format(name, arg1, axis,
                                                          kwargs.get('keepdims')))

run_test(5)
run_test([2, 3])
run_test([[2, -3], [-6, 7]])
run_test([[2, -3], [-6, 7]], axis=0)
run_test([[2, -3], [-6, 7]], axis=0, keepdims=True)
run_test([[2, -3], [-6, 7]], axis=1)
run_test([[2, -3], [-6, 7]], axis=1, keepdims=True)
run_test([[2, -3], [-6, 7]], axis=(0, 1))
run_test([[2, -3], [-6, 7]], axis=(1, 0))
