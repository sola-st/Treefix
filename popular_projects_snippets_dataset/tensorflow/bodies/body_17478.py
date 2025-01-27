# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Assigns a new value to this variable.

    Args:
      value: A `Tensor`. The new value for this variable.
      use_locking: If `True`, use locking during the assignment.
      name: The name to use for the assignment.
      read_value: A `bool`. Whether to read and return the new value of the
        variable or not.

    Returns:
      If `read_value` is `True`, this method will return the new value of the
      variable after the assignment has completed. Otherwise, when in graph mode
      it will return the `Operation` that does the assignment, and when in eager
      mode it will return `None`.
    """
# Note: not depending on the cached value here since this can be used to
# initialize the variable.
with _handle_graph(self.handle):
    value_tensor = ops.convert_to_tensor(value, dtype=self.dtype)
    if not self._shape.is_compatible_with(value_tensor.shape):
        if self.name is None:
            tensor_name = ""
        else:
            tensor_name = " " + str(self.name)
        raise ValueError(
            (f"Cannot assign value to variable '{tensor_name}': Shape mismatch."
             f"The variable shape {self._shape}, and the "
             f"assigned value shape {value_tensor.shape} are incompatible."))
    kwargs = {}
    if forward_compat.forward_compatible(2022, 3, 23):
        # If the shape is fully defined, we do a runtime check with the shape of
        # value.
        validate_shape = self._validate_shape and self._shape.is_fully_defined()
        kwargs["validate_shape"] = validate_shape
    assign_op = gen_resource_variable_ops.assign_variable_op(
        self.handle, value_tensor, name=name, **kwargs)
    if read_value:
        exit(self._lazy_read(assign_op))
exit(assign_op)
