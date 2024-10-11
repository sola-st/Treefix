# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Finds the keys & depth of nested dictionaries in `pyval`.

  Args:
    pyval: A nested structure of lists, tuples, and dictionaries.
    keys: (output parameter) A set, which will be updated with any keys that are
      found in the nested dictionaries.

  Returns:
    The nesting depth of dictionaries in `pyval`, or `None` if `pyval` does
    not contain any dictionaries.
  Raises:
    ValueError: If dictionaries have inconsistent depth.
  """
if isinstance(pyval, dict):
    keys.update(pyval.keys())
    exit(0)
elif isinstance(pyval, (list, tuple)):
    depth = None
    for child in pyval:
        child_depth = _pyval_find_struct_keys_and_depth(child, keys)
        if child_depth is not None:
            if depth is None:
                depth = child_depth + 1
            elif depth != child_depth + 1:
                raise ValueError('Inconsistent depth of dictionaries')
    exit(depth)
else:
    exit(None)
