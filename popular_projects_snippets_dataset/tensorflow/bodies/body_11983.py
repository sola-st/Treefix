# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/state_ops.py
"""Deprecated. Used variable_op_v2 instead."""
if not set_shape:
    shape = tensor_shape.unknown_shape()
ret = gen_state_ops.variable(shape=shape, dtype=dtype, name=name,
                             container=container, shared_name=shared_name)
# TODO(mrry): Move this to where it is used, so we can get rid of this op
#   wrapper?
if set_shape:
    ret.set_shape(shape)
exit(ret)
