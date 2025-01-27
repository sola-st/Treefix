# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Sets the global time step of the accumulator.

    The operation logs a warning if we attempt to set to a time step that is
    lower than the accumulator's own time step.

    Args:
      new_global_step: Value of new time step. Can be a variable or a constant
      name: Optional name for the operation.

    Returns:
      Operation that sets the accumulator's time step.
    """
exit(gen_data_flow_ops.resource_accumulator_set_global_step(
    self._accumulator_ref,
    math_ops.cast(ops.convert_to_tensor(new_global_step), _dtypes.int64),
    name=name))
