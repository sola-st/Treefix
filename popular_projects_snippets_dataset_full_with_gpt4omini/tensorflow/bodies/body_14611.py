# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(condition, arr, *args, **kwargs):
    for fn1 in self.array_transforms:
        for fn2 in self.array_transforms:
            arg1 = fn1(condition)
            arg2 = fn2(arr)
            self.match(
                np_array_ops.compress(arg1, arg2, *args, **kwargs),
                np.compress(
                    np.asarray(arg1).astype(np.bool_), arg2, *args, **kwargs))

run_test([True], 5)
run_test([False], 5)
run_test([], 5)
run_test([True, False, True], [1, 2, 3])
run_test([True, False], [1, 2, 3])
run_test([False, True], [[1, 2], [3, 4]])
run_test([1, 0, 1], [1, 2, 3])
run_test([1, 0], [1, 2, 3])
run_test([0, 1], [[1, 2], [3, 4]])
run_test([True], [[1, 2], [3, 4]])
run_test([False, True], [[1, 2], [3, 4]], axis=1)
run_test([False, True], [[1, 2], [3, 4]], axis=0)
run_test([False, True], [[1, 2], [3, 4]], axis=-1)
run_test([False, True], [[1, 2], [3, 4]], axis=-2)
