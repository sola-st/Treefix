# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest.py
"""Helper function for pack_nest_as.

  Args:
    structure: Substructure (tuple of elements and/or tuples) to mimic
    flat: Flattened values to output substructure for.
    index: Index at which to start reading from flat.

  Returns:
    The tuple (new_index, child), where:
      * new_index - the updated index into `flat` having processed `structure`.
      * packed - the subset of `flat` corresponding to `structure`,
                 having started at `index`, and packed into the same nested
                 format.

  Raises:
    ValueError: if `structure` contains more elements than `flat`
      (assuming indexing starts from `index`).
  """
packed = []
for s in _yield_value(structure):
    if is_nested(s):
        new_index, child = _packed_nest_with_indices(s, flat, index)
        packed.append(nest._sequence_like(s, child))  # pylint: disable=protected-access
        index = new_index
    else:
        packed.append(flat[index])
        index += 1
exit((index, packed))
