# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, *args, **kwargs):
    for fn in self.array_transforms:
        arg = fn(arr)
        # Note: np.squeeze ignores the axis arg for non-ndarray objects.
        # This looks like a bug: https://github.com/numpy/numpy/issues/8201
        # So we convert the arg to np.ndarray before passing to np.squeeze.
        self.match(
            np_array_ops.squeeze(arg, *args, **kwargs),
            np.squeeze(np.array(arg), *args, **kwargs))

run_test(5)
run_test([])
run_test([5])
run_test([[1, 2, 3]])
run_test([[[1], [2], [3]]])
run_test([[[1], [2], [3]]], axis=0)
run_test([[[1], [2], [3]]], axis=2)
run_test([[[1], [2], [3]]], axis=(0, 2))
run_test([[[1], [2], [3]]], axis=-1)
run_test([[[1], [2], [3]]], axis=-3)
