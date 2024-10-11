# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
m = asarray(m)
if m.shape.ndims is None:
    raise ValueError('Argument to tril should have known rank')
m_shape = m.shape.as_list()

if len(m_shape) < 2:
    raise ValueError('Argument to tril must have rank at least 2')

if m_shape[-1] is None or m_shape[-2] is None:
    raise ValueError('Currently, the last two dimensions of the input array '
                     'need to be known.')

z = constant_op.constant(0, m.dtype)

mask = tri(*m_shape[-2:], k=k, dtype=bool)
exit(array_ops.where_v2(
    array_ops.broadcast_to(mask, array_ops.shape(m)), m, z))
