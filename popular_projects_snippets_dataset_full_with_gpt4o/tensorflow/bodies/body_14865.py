# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
array_transforms = [
    lambda x: x,  # Identity,
    ops.convert_to_tensor,
    np.array,
    lambda x: np.array(x, dtype=np.float32),
    lambda x: np.array(x, dtype=np.float64),
    np_array_ops.array,
    lambda x: np_array_ops.array(x, dtype=np.float32),
    lambda x: np_array_ops.array(x, dtype=np.float64)
]

def run_test(start, stop, **kwargs):
    for fn1 in array_transforms:
        for fn2 in array_transforms:
            arg1 = fn1(start)
            arg2 = fn2(stop)
            self.match(
                np_math_ops.linspace(arg1, arg2, **kwargs),
                np.linspace(arg1, arg2, **kwargs),
                msg='linspace({}, {})'.format(arg1, arg2))

run_test(0, 1)
run_test(0, 1, num=10)
run_test(0, 1, endpoint=False)
run_test(0, -1)
run_test(0, -1, num=10)
run_test(0, -1, endpoint=False)
