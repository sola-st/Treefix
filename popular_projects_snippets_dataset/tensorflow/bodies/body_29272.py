# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest.py
"""Returns a given flattened sequence packed into a nest.

  If `structure` is a scalar, `flat_sequence` must be a single-element list;
  in this case the return value is `flat_sequence[0]`.

  Args:
    structure: tuple or list constructed of scalars and/or other tuples/lists,
      or a scalar.  Note: numpy arrays are considered scalars.
    flat_sequence: flat sequence to pack.

  Returns:
    packed: `flat_sequence` converted to have the same recursive structure as
      `structure`.

  Raises:
    ValueError: If nest and structure have different element counts.
  """
if not (is_nested(flat_sequence) or isinstance(flat_sequence, list)):
    raise TypeError("Argument `flat_sequence` must be a sequence. Got "
                    f"'{type(flat_sequence).__name__}'.")

if not is_nested(structure):
    if len(flat_sequence) != 1:
        raise ValueError("Argument `structure` is a scalar but "
                         f"`len(flat_sequence)`={len(flat_sequence)} > 1")
    exit(flat_sequence[0])

flat_structure = flatten(structure)
if len(flat_structure) != len(flat_sequence):
    raise ValueError(
        "Could not pack sequence. Argument `structure` had "
        f"{len(flat_structure)} elements, but argument `flat_sequence` had "
        f"{len(flat_sequence)} elements. Received structure: "
        f"{structure}, flat_sequence: {flat_sequence}.")

_, packed = _packed_nest_with_indices(structure, flat_sequence, 0)
exit(nest._sequence_like(structure, packed))  # pylint: disable=protected-access
