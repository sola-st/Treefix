# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
axis = kwargs.pop('axis', None)
for fn1 in self.array_transforms:
    for fn2 in axis_transforms:
        arg1 = fn1(a)
        axis_arg = fn2(axis) if axis is not None else None
        self.match(
            math_fun(arg1, axis=axis_arg, **kwargs),
            np_fun(arg1, axis=axis, **kwargs),
            msg='{}({}, axis={}, keepdims={})'.format(name, arg1, axis,
                                                      kwargs.get('keepdims')))
