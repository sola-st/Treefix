# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, *args, **kwargs):
    for fn in self.array_transforms:
        arg = fn(arr)
        self.match(
            np_array_ops.cumprod(arg, *args, **kwargs),
            np.cumprod(arg, *args, **kwargs))
        self.match(
            np_array_ops.cumsum(arg, *args, **kwargs),
            np.cumsum(arg, *args, **kwargs))

run_test([])
run_test([1, 2, 3])
run_test([1, 2, 3], dtype=float)
run_test([1, 2, 3], dtype=np.float32)
run_test([1, 2, 3], dtype=np.float64)
run_test([1., 2., 3.])
run_test([1., 2., 3.], dtype=int)
run_test([1., 2., 3.], dtype=np.int32)
run_test([1., 2., 3.], dtype=np.int64)
run_test([[1, 2], [3, 4]], axis=1)
run_test([[1, 2], [3, 4]], axis=0)
run_test([[1, 2], [3, 4]], axis=-1)
run_test([[1, 2], [3, 4]], axis=-2)
