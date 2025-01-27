# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, repeats, *args, **kwargs):
    for fn1 in self.array_transforms:
        for fn2 in self.array_transforms:
            arr_arg = fn1(arr)
            repeats_arg = fn2(repeats)
            self.match(
                np_array_ops.repeat(arr_arg, repeats_arg, *args, **kwargs),
                np.repeat(arr_arg, repeats_arg, *args, **kwargs))

run_test(1, 2)
run_test([1, 2], 2)
run_test([1, 2], [2])
run_test([1, 2], [1, 2])
run_test([[1, 2], [3, 4]], 3, axis=0)
run_test([[1, 2], [3, 4]], 3, axis=1)
run_test([[1, 2], [3, 4]], [3], axis=0)
run_test([[1, 2], [3, 4]], [3], axis=1)
run_test([[1, 2], [3, 4]], [3, 2], axis=0)
run_test([[1, 2], [3, 4]], [3, 2], axis=1)
run_test([[1, 2], [3, 4]], [3, 2], axis=-1)
run_test([[1, 2], [3, 4]], [3, 2], axis=-2)
