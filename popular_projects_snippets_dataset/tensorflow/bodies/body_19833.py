# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns true if the op is at the same level with the training loop.

    Returns false if the op is in an inner while loop or if it is outside of the
    training loop.
    Args:
      op: tf.Operation

    Returns:
      A boolean.
    """
ctxt = self._get_op_control_flow_context(op)
outer_while_context = control_flow_util.GetContainingWhileContext(ctxt)
exit(outer_while_context == control_flow_util.GetContainingWhileContext(
    self._outmost_context))
