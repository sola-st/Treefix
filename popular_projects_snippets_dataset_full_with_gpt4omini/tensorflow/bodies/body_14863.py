# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py

def run_test(arr, *args, **kwargs):
    for fn in self.array_transforms:
        arg = fn(arr)
        self.match(
            np_math_ops.ptp(arg, *args, **kwargs), np.ptp(arg, *args, **kwargs))

run_test([1, 2, 3])
run_test([1., 2., 3.])
run_test([[1, 2], [3, 4]], axis=1)
run_test([[1, 2], [3, 4]], axis=0)
run_test([[1, 2], [3, 4]], axis=-1)
run_test([[1, 2], [3, 4]], axis=-2)
