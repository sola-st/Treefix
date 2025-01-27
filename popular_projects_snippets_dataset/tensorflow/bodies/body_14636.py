# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, *args, **kwargs):
    for fn in self.array_transforms:
        arg = fn(arr)
        self.match(
            np_array_ops.ravel(arg, *args, **kwargs),
            np.ravel(arg, *args, **kwargs))

run_test(5)
run_test(5.)
run_test([])
run_test([[]])
run_test([[], []])
run_test([1, 2, 3])
run_test([1., 2., 3.])
run_test([[1, 2], [3, 4]])
run_test(np.arange(8).reshape((2, 2, 2)).tolist())
