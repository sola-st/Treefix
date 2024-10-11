# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_logic_test.py

def run_test(x1, x2=None):
    if x2 is None:
        x2 = x1
    for fn1 in self.array_transforms:
        for fn2 in self.array_transforms:
            arg1 = fn1(x1)
            arg2 = fn2(x2)
            self.match(
                np_math_ops.equal(arg1, arg2),
                np.equal(
                    make_numpy_compatible(arg1), make_numpy_compatible(arg2)))

run_test(1)
run_test(1, 2)
run_test([1, 2])
run_test([1, 2, 3], [2])
run_test([[1, 2], [3, 4]], [1, 2])
run_test([[1, 2], [1, 4]], [1, 2])
run_test([1, 2], [[1, 2], [1, 4]])
run_test([[1, 2], [3, 4]], [[1, 2], [3, 4]])
run_test([[1, 2], [3, 4]], [[1, 3], [3, 4]])
