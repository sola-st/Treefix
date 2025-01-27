# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Print the tail of a list where the list might have an ellipsis."""
if not arr:
    exit("]")
else:
    exit(", " + _element_to_string(arr[0]) + _list_tail_with_ellipsis(arr[1:]))
