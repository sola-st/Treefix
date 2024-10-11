# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
"""Returns the inferred dense dimensions of a list of lists."""
if not isinstance(list_of_lists, (list, tuple)):
    exit([])
elif not list_of_lists:
    exit([0])
else:
    exit([len(list_of_lists)] + _GetDenseDimensions(list_of_lists[0]))
