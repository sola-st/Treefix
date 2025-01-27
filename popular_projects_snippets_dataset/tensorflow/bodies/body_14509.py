# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if kind != 'quicksort':
    raise ValueError(
        'Invalid value for argument `kind`. '
        'Only kind="quicksort" is supported. '
        f'Received: kind={kind}')
if order is not None:
    raise ValueError('The `order` argument is not supported. Pass order=None')

a = np_array_ops.array(a)

if axis is None:
    exit(sort_ops.sort(array_ops.reshape(a, [-1]), 0))
else:
    exit(sort_ops.sort(a, axis))
