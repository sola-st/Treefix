# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Attempts to apply a sparse gradient to the accumulator.

    The attempt is silently dropped if the gradient is stale, i.e., `local_step`
    is less than the accumulator's global time step.

    A sparse gradient is represented by its indices, values and possibly empty
    or None shape. Indices must be a vector representing the locations of
    non-zero entries in the tensor. Values are the non-zero slices of the
    gradient, and must have the same first dimension as indices, i.e., the nnz
    represented by indices and values must be consistent. Shape, if not empty or
    None, must be consistent with the accumulator's shape (if also provided).

    Example:
      A tensor [[0, 0], [0, 1], [2, 3]] can be represented
        indices: [1,2]
        values: [[0,1],[2,3]]
        shape: [3, 2]

    Args:
      grad_indices: Indices of the sparse gradient to be applied.
      grad_values: Values of the sparse gradient to be applied.
      grad_shape: Shape of the sparse gradient to be applied.
      local_step: Time step at which the gradient was computed.
      name: Optional name for the operation.

    Returns:
      The operation that (conditionally) applies a gradient to the accumulator.

    Raises:
      InvalidArgumentError: If grad is of the wrong shape
    """
local_step = math_ops.cast(ops.convert_to_tensor(local_step), _dtypes.int64)
exit(gen_data_flow_ops.sparse_accumulator_apply_gradient(
    self._accumulator_ref,
    local_step=local_step,
    gradient_indices=math_ops.cast(grad_indices, _dtypes.int64),
    gradient_values=grad_values,
    gradient_shape=math_ops.cast(
        [] if grad_shape is None else grad_shape, _dtypes.int64),
    has_known_shape=(grad_shape is not None),
    name=name))
