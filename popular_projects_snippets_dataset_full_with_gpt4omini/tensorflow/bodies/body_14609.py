# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, *args, **kwargs):
    for fn in self.array_transforms:
        arr = fn(arr)
        self.match(
            np_array_ops.all(arr, *args, **kwargs),
            np.all(arr, *args, **kwargs))
        self.match(
            np_array_ops.any(arr, *args, **kwargs),
            np.any(arr, *args, **kwargs))

run_test(0)
run_test(1)
run_test([])
run_test([[True, False], [True, True]])
run_test([[True, False], [True, True]], axis=0)
run_test([[True, False], [True, True]], axis=0, keepdims=True)
run_test([[True, False], [True, True]], axis=1)
run_test([[True, False], [True, True]], axis=1, keepdims=True)
run_test([[True, False], [True, True]], axis=(0, 1))
run_test([[True, False], [True, True]], axis=(0, 1), keepdims=True)
run_test([5.2, 3.5], axis=0)
run_test([1, 0], axis=0)
