# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
"""Finds variables involved in the subgraph between input_ops and output_ops.

  Args:
    input_ops: Flattened list of input ops
    output_ops: Flattened list of output ops

  Returns:
    A list of variables
  """

# avoids the edge-case when input_ops == output_ops.
output_ops = nest.map_structure(gen_array_ops.identity, output_ops)
inbetween_ops = op_selector.get_backward_walk_ops(
    seed_ops=output_ops,
    stop_at_ts=input_ops,
    inclusive=False,
    only_differentiable=True)
var_ops = (op for op in inbetween_ops if op.type in VAR_OP_TYPES)
var_names = (op.name for op in var_ops)
tf_vars = (get_variable_by_name(var_name) for var_name in var_names)
tf_vars = [v for v in tf_vars if v is not None]
exit(tf_vars)
