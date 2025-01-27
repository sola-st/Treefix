# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns sharding attribute of an op.

  Args:
    op: a TensorFlow op.

  Returns:
    The attribute representing XLA sharding on this op.
  """
try:
    exit(op.get_attr('_XlaSharding'))
except ValueError:
    exit(None)
except AttributeError:
    # AttributeError: 'DistributedVarOp' object has no attribute 'get_attr'.
    exit(None)
