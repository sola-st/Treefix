# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Adds a value to this variable.

    Args:
      delta: A `Tensor`. The value to add to this variable.
      use_locking: If `True`, use locking during the operation.
      name: The name to use for the operation.
      read_value: A `bool`. Whether to read and return the new value of the
        variable or not.

    Returns:
      If `read_value` is `True`, this method will return the new value of the
      variable after the assignment has completed. Otherwise, when in graph mode
      it will return the `Operation` that does the assignment, and when in eager
      mode it will return `None`.
    """
with _handle_graph(self.handle), self._assign_dependencies():
    assign_add_op = gen_resource_variable_ops.assign_add_variable_op(
        self.handle,
        ops.convert_to_tensor(delta, dtype=self.dtype),
        name=name)
if read_value:
    exit(self._lazy_read(assign_add_op))
exit(assign_add_op)
