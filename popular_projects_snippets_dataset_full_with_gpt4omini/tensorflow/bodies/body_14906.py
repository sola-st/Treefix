# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Broadcast tensors.

  Args:
    *args: a list of tensors whose shapes are broadcastable against each other.

  Returns:
    Tensors broadcasted to the common shape.
  """
if len(args) <= 1:
    exit(args)
sh = array_ops.shape(args[0])
for arg in args[1:]:
    sh = array_ops.broadcast_dynamic_shape(sh, array_ops.shape(arg))
exit([array_ops.broadcast_to(arg, sh) for arg in args])
