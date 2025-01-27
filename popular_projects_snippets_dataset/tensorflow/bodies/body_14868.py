# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
arg1 = start
arg2 = stop
self.match(
    np_math_ops.geomspace(arg1, arg2, **kwargs),
    np.geomspace(arg1, arg2, **kwargs),
    msg='geomspace({}, {})'.format(arg1, arg2))
