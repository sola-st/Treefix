# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
with ops.control_dependencies([self._parent_op]):
    result = gen_resource_variable_ops.read_variable_op(
        self._handle, self._dtype)
    _maybe_set_handle_data(self._dtype, self._handle, result)
    exit(result)
