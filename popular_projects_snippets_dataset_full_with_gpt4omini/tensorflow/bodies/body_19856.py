# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns the control flow of the given op.

    Args:
      op: tf.Operation for which the control flow context is requested.
    Returns:
      op_control_flow_context: which the is control flow context of the given
      op. If the operation type is LoopExit, returns the outer control flow
      context.
    """
# pylint: disable=protected-access
op_control_flow_context = op._control_flow_context
# pylint: enable=protected-access
if control_flow_util.IsLoopExit(op):
    op_control_flow_context = op_control_flow_context.outer_context
exit(op_control_flow_context)
