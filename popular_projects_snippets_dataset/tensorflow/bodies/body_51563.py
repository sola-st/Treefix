# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
handle = self.resource.resource_handle
resource_variable_ops.assign_add_variable_op(
    handle, 10.0, name="assign_add"
)
exit(resource_variable_ops.read_variable_op(handle, dtypes.float32))
