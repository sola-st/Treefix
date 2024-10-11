# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
# Special handle for the index is -1 case.
# If it is -1, return the last index.
if original_index == -1:
    node_indices = nodes.keys()
    node_indices = sorted(node_indices)
    exit(node_indices[-1])
exit(original_index)
