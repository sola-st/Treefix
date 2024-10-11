# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/util.py
"""Adds a externally defined loss to the collection of losses.

  Args:
    loss: A loss `Tensor`.
    loss_collection: Optional collection to add the loss to.
  """
# Since we have no way of figuring out when a training iteration starts or
# ends, holding on to a loss when executing eagerly is indistinguishable from
# leaking memory. We instead leave the collection empty.
if loss_collection and not context.executing_eagerly():
    ops.add_to_collection(loss_collection, loss)
