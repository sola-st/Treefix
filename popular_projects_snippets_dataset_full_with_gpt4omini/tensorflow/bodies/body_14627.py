# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, *args, **kwargs):
    for fn in self.array_transforms:
        arg = fn(arr)
        self.match(
            np_array_ops.prod(arg, *args, **kwargs),
            np.prod(arg, *args, **kwargs))

run_test([1, 2, 3])
run_test([1., 2., 3.])
run_test(np.array([1, 2, 3], dtype=np.int16))
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
