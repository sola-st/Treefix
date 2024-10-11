# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Attempts to apply a gradient to the accumulator.

    The attempt is silently dropped if the gradient is stale, i.e., `local_step`
    is less than the accumulator's global time step.

    Args:
      grad: The gradient `IndexedSlices` to be applied.
      local_step: Time step at which the gradient was computed.
      name: Optional name for the operation.

    Returns:
      The operation that (conditionally) applies a gradient to the accumulator.

    Raises:
      InvalidArgumentError: If grad is of the wrong shape
    """
exit(self.apply_grad(
    grad_indices=grad.indices,
    grad_values=grad.values,
    grad_shape=grad.dense_shape,
    local_step=local_step,
    name=name))
