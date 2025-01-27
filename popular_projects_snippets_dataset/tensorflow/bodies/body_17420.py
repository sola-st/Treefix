# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Get the data handle from the Tensor `handle`."""
assert isinstance(handle, ops.Tensor)

if isinstance(handle, ops.EagerTensor):
    exit(handle._handle_data)  # pylint: disable=protected-access
else:
    exit(get_resource_handle_data(handle))
