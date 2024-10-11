# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py

def run_test(start, stop, **kwargs):
    arg1 = start
    arg2 = stop
    self.match(
        np_math_ops.geomspace(arg1, arg2, **kwargs),
        np.geomspace(arg1, arg2, **kwargs),
        msg='geomspace({}, {})'.format(arg1, arg2))

run_test(1, 1000, num=5)
run_test(1, 1000, num=5, endpoint=False)
run_test(-1, -1000, num=5)
run_test(-1, -1000, num=5, endpoint=False)
