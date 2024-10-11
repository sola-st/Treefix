# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Obtains HandleData from a tensor."""
if isinstance(source_t, EagerTensor):
    exit(source_t._handle_data)  # pylint: disable=protected-access
exit(get_resource_handle_data(source_t))
