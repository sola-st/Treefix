# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, axes=None):
    for fn1 in self.array_transforms:
        for fn2 in self.array_transforms:
            arr_arg = fn1(arr)
            axes_arg = fn2(axes) if axes is not None else None
            self.match(
                np_array_ops.transpose(arr_arg, axes_arg),
                np.transpose(arr_arg, axes))

run_test(5)
run_test([])
run_test([5])
run_test([5, 6, 7])
run_test(np.arange(30).reshape(2, 3, 5).tolist())
run_test(np.arange(30).reshape(2, 3, 5).tolist(), [0, 1, 2])
run_test(np.arange(30).reshape(2, 3, 5).tolist(), [0, 2, 1])
run_test(np.arange(30).reshape(2, 3, 5).tolist(), [1, 0, 2])
run_test(np.arange(30).reshape(2, 3, 5).tolist(), [1, 2, 0])
run_test(np.arange(30).reshape(2, 3, 5).tolist(), [2, 0, 1])
run_test(np.arange(30).reshape(2, 3, 5).tolist(), [2, 1, 0])
