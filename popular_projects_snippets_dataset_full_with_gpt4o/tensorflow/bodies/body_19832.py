# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns true if the given op is inside a tf.cond or in tf.while_loop.

    Args:
      op: A tensorflow op that should be checked whether in control flow or not.
    Returns:
      A boolean value whether the op is in control flow or not.
    """
exit(control_flow_util.IsInCond(op))
