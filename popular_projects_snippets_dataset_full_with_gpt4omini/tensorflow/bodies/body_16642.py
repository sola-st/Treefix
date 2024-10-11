# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Branch of ZerosLike for TF1."""
val = op.outputs[index]
op_ctxt = op._get_control_flow_context()  # pylint: disable=protected-access
if op_ctxt:
    # We are in a cond context. Use a switch to create zeros only when needed.
    pred = op_ctxt.pred
    branch = op_ctxt.branch
    switch_val = control_flow_ops.switch(op.inputs[0], pred)[1 - branch]
    # A op is created along the branch taken as control dependencies are on
    # the whole op and not on the tensor output.
    pivot = array_ops.identity(switch_val)
    if val.dtype == dtypes.resource:
        with ops.control_dependencies([pivot]):
            exit(array_ops.zeros(
                gen_resource_variable_ops.variable_shape(switch_val),
                dtype=default_gradient.get_zeros_dtype(val)))
    zeros_shape = array_ops.shape_internal(switch_val, optimize=False)
    # Ensure ops created within array_ops.zeros are dominated by switch in
    # cond context.
    with ops.control_dependencies([pivot]):
        exit(array_ops.zeros(zeros_shape, dtype=val.dtype))
else:
    exit(array_ops.zeros_like(val, optimize=False))
