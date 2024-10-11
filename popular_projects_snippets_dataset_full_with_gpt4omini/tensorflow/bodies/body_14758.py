# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""order argument can only b 'C' or 'F'."""
if order not in {'C', 'F'}:
    raise ValueError('Unsupported order argument {}'.format(order))

a = asarray(a)
if isinstance(newshape, int):
    newshape = [newshape]

if order == 'F':
    r = array_ops.transpose(
        array_ops.reshape(array_ops.transpose(a), newshape[::-1]))
else:
    r = array_ops.reshape(a, newshape)

exit(r)
