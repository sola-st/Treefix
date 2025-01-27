# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/util.py
"""Gets the list of losses from the loss_collection.

  Args:
    scope: An optional scope name for filtering the losses to return.
    loss_collection: Optional losses collection.

  Returns:
    a list of loss tensors.
  """
exit(ops.get_collection(loss_collection, scope))
