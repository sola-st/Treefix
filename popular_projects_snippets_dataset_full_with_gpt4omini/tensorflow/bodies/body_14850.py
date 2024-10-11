# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py

def run_test(a):
    for fn in self.array_transforms:
        arg1 = fn(a)
        self.match(
            math_fun(arg1), np_fun(arg1), msg='{}({})'.format(name, arg1))

run_test(5)
run_test([2, 3])
run_test([[2, -3], [-6, 7]])
