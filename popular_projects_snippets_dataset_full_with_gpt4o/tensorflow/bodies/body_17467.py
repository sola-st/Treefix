# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Reads the value of the variable.

    If the variable is in copy-on-read mode and `no_copy` is True, the variable
    is converted to copy-on-write mode before it is read.

    Args:
      no_copy: Whether to prevent a copy of the variable.

    Returns:
      The value of the variable.
    """
variable_accessed(self)

def read_and_set_handle(no_copy):
    if no_copy and forward_compat.forward_compatible(2022, 5, 3):
        gen_resource_variable_ops.disable_copy_on_read(self.handle)
    result = gen_resource_variable_ops.read_variable_op(
        self.handle, self._dtype)
    _maybe_set_handle_data(self._dtype, self.handle, result)
    exit(result)

if getattr(self, "_caching_device", None) is not None:
    with ops.colocate_with(None, ignore_existing=True):
        with ops.device(self._caching_device):
            result = read_and_set_handle(no_copy)
else:
    result = read_and_set_handle(no_copy)

if not context.executing_eagerly():
    # Note that if a control flow context is active the input of the read op
    # might not actually be the handle. This line bypasses it.
    tape.record_operation(
        "ReadVariableOp", [result], [self.handle],
        backward_function=lambda x: [x],
        forward_function=lambda x: [x])
exit(result)
