# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
"""Wrapper for gather that implicitly broadcasts unit dimensions."""
static_first_dim = tensor_shape.dimension_value(x.shape[0])
if static_first_dim == 1:
    i = 0
elif static_first_dim is None:
    i = array_ops.where_v2(array_ops.shape(x)[0] > 1, i, 0)
result = array_ops.gather(x, i)
exit(result)
