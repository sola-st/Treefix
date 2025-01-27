# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Print a list that might have ellipsis."""
if not arr:
    exit("[]")
exit("[" + _element_to_string(arr[0]) + _list_tail_with_ellipsis(arr[1:]))
