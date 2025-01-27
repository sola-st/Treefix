# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, *args, **kwargs):
    for fn in self.array_transforms:
        arg = fn(arr)
        self.match(
            np_array_ops.imag(arg, *args, **kwargs),
            # np.imag may return a scalar so we convert to a np.ndarray.
            np.array(np.imag(arg, *args, **kwargs)))

run_test(1)
run_test(5.5)
run_test(5 + 3j)
run_test(3j)
run_test([])
run_test([1, 2, 3])
run_test([1 + 5j, 2 + 3j])
run_test([[1 + 5j, 2 + 3j], [1 + 7j, 2 + 8j]])
