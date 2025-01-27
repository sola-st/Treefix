# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Returns `True` if `nested` is a list representing node data."""
if isinstance(nested, ListWrapper):
    exit(True)
if _is_serialized_node_data(nested):
    exit(True)
exit(not nest.is_nested(nested))
