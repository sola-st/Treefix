# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if no_copy and forward_compat.forward_compatible(2022, 5, 3):
    gen_resource_variable_ops.disable_copy_on_read(self.handle)
result = gen_resource_variable_ops.read_variable_op(
    self.handle, self._dtype)
_maybe_set_handle_data(self._dtype, self.handle, result)
exit(result)
