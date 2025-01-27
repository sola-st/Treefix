# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/util.py
"""Gets the list of regularization losses.

  Args:
    scope: An optional scope name for filtering the losses to return.

  Returns:
    A list of regularization losses as Tensors.
  """
exit(ops.get_collection(ops.GraphKeys.REGULARIZATION_LOSSES, scope))
