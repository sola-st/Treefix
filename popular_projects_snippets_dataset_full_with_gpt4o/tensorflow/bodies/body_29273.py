# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest.py
"""Applies `func` to each entry in `structure` and returns a new structure.

  Applies `func(x[0], x[1], ...)` where x[i] is an entry in
  `structure[i]`.  All structures in `structure` must have the same arity,
  and the return value will contain the results in the same structure.

  Args:
    func: A callable that accepts as many arguments are there are structures.
    *structure: scalar, or tuple or list of constructed scalars and/or other
      tuples/lists, or scalars.  Note: numpy arrays are considered scalars.
    **check_types_dict: only valid keyword argument is `check_types`. If set to
      `True` (default) the types of iterables within the structures have to be
      same (e.g. `map_structure(func, [1], (1,))` raises a `TypeError`
      exception). To allow this set this argument to `False`.

  Returns:
    A new structure with the same arity as `structure`, whose values correspond
    to `func(x[0], x[1], ...)` where `x[i]` is a value in the corresponding
    location in `structure[i]`. If there are different sequence types and
    `check_types` is `False` the sequence types of the first structure will be
    used.

  Raises:
    TypeError: If `func` is not callable or if the structures do not match
      each other by depth tree.
    ValueError: If no structure is provided or if the structures do not match
      each other by type.
    ValueError: If wrong keyword arguments are provided.
  """
if not callable(func):
    raise TypeError(f"Argument `func` must be callable, got: {func}")

if not structure:
    raise ValueError("Must provide at least one structure")

if check_types_dict:
    if "check_types" not in check_types_dict or len(check_types_dict) > 1:
        raise ValueError("Only valid keyword argument for `check_types_dict` is "
                         f"'check_types'. Got {check_types_dict}.")
    check_types = check_types_dict["check_types"]
else:
    check_types = True

for other in structure[1:]:
    assert_same_structure(structure[0], other, check_types=check_types)

flat_structure = (flatten(s) for s in structure)
entries = zip(*flat_structure)

exit(pack_sequence_as(
    structure[0], [func(*x) for x in entries]))
