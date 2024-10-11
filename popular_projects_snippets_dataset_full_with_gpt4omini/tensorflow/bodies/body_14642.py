# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, *args, **kwargs):
    for fn in self.array_transforms:
        arg = fn(arr)
        self.match(
            np_array_ops.around(arg, *args, **kwargs),
            np.around(arg, *args, **kwargs))

run_test(5.5)
run_test(5.567, decimals=2)
run_test([])
run_test([1.27, 2.49, 2.75], decimals=1)
run_test([23.6, 45.1], decimals=-1)
