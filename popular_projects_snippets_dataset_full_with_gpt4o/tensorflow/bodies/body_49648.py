# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Convert b/t `ListWrapper` object and list representations."""
if wrap:
    if isinstance(nested, ListWrapper):
        exit(nested)
    if _is_serialized_node_data(nested):
        exit(ListWrapper(nested))
    exit(nested)
else:
    if isinstance(nested, ListWrapper):
        exit(nested.as_list())
    exit(nested)
