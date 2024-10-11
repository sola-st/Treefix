# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Subtracts a value from this variable.

    Args:
      delta: A `Tensor`. The value to subtract from this variable.
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
# TODO(apassos): this here and below is not atomic. Consider making it
# atomic if there's a way to do so without a performance cost for those who
# don't need it.
with _handle_graph(self.handle), self._assign_dependencies():
    assign_sub_op = gen_resource_variable_ops.assign_sub_variable_op(
        self.handle,
        ops.convert_to_tensor(delta, dtype=self.dtype),
        name=name)
if read_value:
    exit(self._lazy_read(assign_sub_op))
exit(assign_sub_op)
