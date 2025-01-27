# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
"""Sets the flag to enable lowering on `op` if necessary.

  Lowering allows cond_v2 and while_v2 to avoid some of the limitations of
  Functions, allowing users to specify devices & colocation inside of cond_v2
  and while_v2 input functions, and enabling non-strict evaluation & partial
  pruning. This brings v2 control flow closer to feature parity with v1 control
  flow.

  However, we do not lower in the following cases:
    - When the `If` or `While` ops are in the XLA context. Because it is easier
      for XLA to apply its own optimizations when dealing with un-lowered
      control flow operators than with low-level control flow primitives.
    - When the eager execution context specifies the executor of functions to
      be the single threaded executor (see context.function_executor_type()).
      Because the single threaded executor does not support v1 control flow ops.
    - When 'lower_using_switch_merge' is explicitly set to False.

  Args:
    op: An `If` or `While` Operation.
    lower_using_switch_merge: Explicit value to lower or not (optional).
  """
if lower_using_switch_merge is not None:
    # pylint: disable=protected-access
    op._set_attr("_lower_using_switch_merge",
                 attr_value_pb2.AttrValue(b=lower_using_switch_merge))
    # pylint: enable=protected-access
elif (not _DISABLE_LOWER_USING_SWITCH_MERGE and
      not control_flow_util.GraphOrParentsInXlaContext(op.graph) and
      context.context().function_call_options.executor_type !=
      "SINGLE_THREADED_EXECUTOR"):
    # pylint: disable=protected-access
    op._set_attr("_lower_using_switch_merge", attr_value_pb2.AttrValue(b=True))
    # pylint: enable=protected-access
