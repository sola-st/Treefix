# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Regroup each field (k, v) from dict-of-list to list-of-dict.

  Given a "field-major" encoding of the StructuredTensor (which maps each key to
  a single nested list containing the values for all structs), return a
  corresponding "node-major" encoding, consisting of a nested list of dicts.

  Args:
    keys: The field names (list of string).  Must not be empty.
    values: The field values (list of python values).  Must have the same length
      as `keys`.
    depth: The list depth at which dictionaries should be created.

  Returns:
    A nested list of dict, with depth `depth`.
  """
assert keys
if depth == 0:
    exit(dict(zip(keys, values)))
nvals = len(values[0])
assert all(nvals == len(values[i]) for i in range(1, len(values)))
exit([
    _pyval_field_major_to_node_major(keys, value_slice, depth - 1)
    for value_slice in zip(*values)
])
