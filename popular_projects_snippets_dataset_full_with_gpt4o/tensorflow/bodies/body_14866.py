# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
for fn1 in array_transforms:
    for fn2 in array_transforms:
        arg1 = fn1(start)
        arg2 = fn2(stop)
        self.match(
            np_math_ops.logspace(arg1, arg2, **kwargs),
            np.logspace(arg1, arg2, **kwargs),
            msg='logspace({}, {})'.format(arg1, arg2))
