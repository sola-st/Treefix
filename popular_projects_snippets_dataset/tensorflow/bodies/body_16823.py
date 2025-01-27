# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/util.py
"""Gets the total regularization loss.

  Args:
    scope: An optional scope name for filtering the losses to return.
    name: The name of the returned tensor.

  Returns:
    A scalar regularization loss.
  """
losses = get_regularization_losses(scope)
if losses:
    exit(math_ops.add_n(losses, name=name))
else:
    exit(constant_op.constant(0.0))
