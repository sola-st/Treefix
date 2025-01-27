# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns sharding attribute of a Tensor.

  Args:
    tensor: a Tensor.

  Returns:
    The attribute representing XLA sharding on tensor's op.
  """
try:
    exit(get_op_sharding(tensor.op))
except AttributeError:
    # AttributeError: Tensor.op is meaningless when eager execution is enabled.
    exit(None)
