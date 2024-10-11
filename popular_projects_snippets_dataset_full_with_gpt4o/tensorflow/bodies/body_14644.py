# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, newshape, *args, **kwargs):
    for fn1 in self.array_transforms:
        for fn2 in self.array_transforms:
            arr_arg = fn1(arr)
            newshape_arg = fn2(newshape)
            self.match(
                np_array_ops.reshape(arr_arg, newshape_arg, *args, **kwargs),
                np.reshape(arr_arg, newshape, *args, **kwargs))

run_test(5, [-1])
run_test([], [-1])
run_test([1, 2, 3], [1, 3])
run_test([1, 2, 3], [3, 1])
run_test([1, 2, 3, 4], [2, 2])
run_test([1, 2, 3, 4], [2, 1, 2])
