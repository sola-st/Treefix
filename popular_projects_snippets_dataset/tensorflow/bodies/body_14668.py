# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, shape):
    for fn in self.array_transforms:
        arg1 = fn(arr)
        self.match(
            np_array_ops.broadcast_to(arg1, shape),
            np.broadcast_to(arg1, shape))

run_test(1, 2)
run_test(1, (2, 2))
run_test([1, 2], (2, 2))
run_test([[1], [2]], (2, 2))
run_test([[1, 2]], (3, 2))
run_test([[[1, 2]], [[3, 4]], [[5, 6]]], (3, 4, 2))
