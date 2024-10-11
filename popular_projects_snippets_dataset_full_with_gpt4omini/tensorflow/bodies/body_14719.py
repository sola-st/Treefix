# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""order, subok and shape arguments mustn't be changed."""
if order != 'K':
    raise ValueError('Non-standard orders are not supported.')
if not subok:
    raise ValueError('subok being False is not supported.')
if shape:
    raise ValueError('Overriding the shape is not supported.')

a = asarray(a)
dtype = dtype or np_utils.result_type(a)
fill_value = asarray(fill_value, dtype=dtype)
exit(array_ops.broadcast_to(fill_value, array_ops.shape(a)))
