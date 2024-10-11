# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Branch of ZerosLike for TF2."""
val = op.outputs[index]
if val.dtype == dtypes.resource:
    exit(array_ops.zeros(
        gen_resource_variable_ops.variable_shape(val),
        dtype=default_gradient.get_zeros_dtype(val)))
if (isinstance(val.op.graph, control_flow_v2_func_graphs.WhileBodyFuncGraph)
    and val.dtype != dtypes.variant):
    # In while_v2 we do not want to add a `ZerosLike` op because that will
    # trigger accumulation of `val`. Normally `ZerosLike` is preferred because
    # it helps avoid creating extra nodes(possibly Consts) for the shape.
    # For variants, we must use ZerosLike.
    if val.shape.is_fully_defined():
        exit(constant_op.constant(0, shape=val.shape.dims, dtype=val.dtype))
    else:
        # Note: Even though we add `Shape` in the default graph, while_v2 is smart
        # enough to place it in the forward graph i.e. `val.graph`.
        zeros_shape = array_ops.shape_internal(val, optimize=False)
        exit(array_ops.zeros(zeros_shape, val.dtype))
else:
    exit(array_ops.zeros_like(val, optimize=False))
