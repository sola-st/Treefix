# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Helper that checks shape compatibility and assigns variable."""
with _handle_graph(handle):
    value_tensor = ops.convert_to_tensor(value)
shape.assert_is_compatible_with(value_tensor.shape)
exit(gen_resource_variable_ops.assign_variable_op(
    handle, value_tensor, name=name))
