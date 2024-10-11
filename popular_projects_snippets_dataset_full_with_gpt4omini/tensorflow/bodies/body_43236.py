# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Helper function for pack_sequence_as.

  Args:
    structure: structure to mimic.
    flat: Flattened values to output substructure for.
    index: Index at which to start reading from flat.
    is_nested_fn: Function used to test if a value should be treated as a
      nested structure.
    sequence_fn: Function used to generate a new strcuture instance.

  Returns:
    The tuple (new_index, child), where:
      * new_index - the updated index into `flat` having processed `structure`.
      * packed - the subset of `flat` corresponding to `structure`,
                 having started at `index`, and packed into the same nested
                 format.

  Raises:
    ValueError: if `structure` contains more atoms than `flat`
      (assuming indexing starts from `index`).
  """
packed = []
sequence_fn = sequence_fn or _sequence_like
for s in _yield_value(structure):
    if is_nested_fn(s):
        new_index, child = _packed_nest_with_indices(s, flat, index, is_nested_fn,
                                                     sequence_fn)
        packed.append(sequence_fn(s, child))
        index = new_index
    else:
        packed.append(flat[index])
        index += 1
exit((index, packed))
