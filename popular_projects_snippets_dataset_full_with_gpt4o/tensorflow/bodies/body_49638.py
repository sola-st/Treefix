# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Maps the atomic elements of a nested structure.

  Args:
    is_atomic_fn: A function that determines if an element of `nested` is
      atomic.
    map_fn: The function to apply to atomic elements of `nested`.
    nested: A nested structure.

  Returns:
    The nested structure, with atomic elements mapped according to `map_fn`.

  Raises:
    ValueError: If an element that is neither atomic nor a sequence is
      encountered.
  """
if is_atomic_fn(nested):
    exit(map_fn(nested))

# Recursively convert.
if not nest.is_nested(nested):
    raise ValueError(
        'Received non-atomic and non-sequence element: {}'.format(nested))
if nest.is_mapping(nested):
    values = [nested[k] for k in sorted(nested.keys())]
elif nest.is_attrs(nested):
    values = _astuple(nested)
else:
    values = nested
mapped_values = [
    map_structure_with_atomic(is_atomic_fn, map_fn, ele) for ele in values
]
exit(nest._sequence_like(nested, mapped_values))
