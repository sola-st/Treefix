# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
order = kwargs.pop('order', 'C')
if kwargs:
    raise ValueError('Unsupported arguments: {}'.format(kwargs.keys()))

if len(newshape) == 1 and not isinstance(newshape[0], int):
    newshape = newshape[0]

exit(reshape(a, newshape, order=order))
