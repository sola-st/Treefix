# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Append the field values from `pyval` to `fields`.

  Args:
    pyval: A python `dict`, or nested list/tuple of `dict`, whose value(s)
      should be appended to `fields`.
    fields: A dictionary mapping string keys to field values.  Field values
      extracted from `pyval` are appended to this dictionary's values.
    depth: The depth at which `pyval` should be appended to the field values.
  """
if not isinstance(pyval, (dict, list, tuple)):
    raise ValueError('Expected dict or nested list/tuple of dict')

for (key, target) in fields.items():
    for _ in range(1, depth):
        target = target[-1]
    target.append(pyval[key] if isinstance(pyval, dict) else [])

if isinstance(pyval, (list, tuple)):
    for child in pyval:
        _pyval_update_fields(child, fields, depth + 1)
