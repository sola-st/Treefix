# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Attempts to apply a gradient to the accumulator.

    The attempt is silently dropped if the gradient is stale, i.e., local_step
    is less than the accumulator's global time step.

    Args:
      grad: The gradient tensor to be applied.
      local_step: Time step at which the gradient was computed.
      name: Optional name for the operation.

    Returns:
      The operation that (conditionally) applies a gradient to the accumulator.

    Raises:
      ValueError: If grad is of the wrong shape
    """
grad = ops.convert_to_tensor(grad, self._dtype)
grad.get_shape().assert_is_compatible_with(self._shape)
local_step = math_ops.cast(ops.convert_to_tensor(local_step), _dtypes.int64)

exit(gen_data_flow_ops.resource_accumulator_apply_gradient(
    self._accumulator_ref, local_step=local_step, gradient=grad, name=name))
