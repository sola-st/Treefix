# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Applies `func` to each entry in `structure` and returns a new structure.

  Applies `func(tuple_path, x[0], x[1], ..., **kwargs)` where `x[i]` is an entry
  in `structure[i]` and `tuple_path` is a tuple of indices and/or dictionary
  keys (as returned by `nest.yield_flat_paths`), which uniquely specifies the
  common path to x[i] in the structures. All structures in `structure` must have
  the same arity, and the return value will contain the results in the same
  structure. Special kwarg `check_types` determines whether the types of
  iterables within the structure must be the same-- see **kwargs definition
  below.

  Args:
    func: A callable with the signature `func(tuple_path, *values, **kwargs)`
      that is evaluated on the leaves of the structure.
    *structure: A variable number of compatible structures to process.
    **kwargs: Optional kwargs to be passed through to func. Special kwarg
      `check_types` is not passed to func, but instead determines whether the
      types of iterables within the structures have to be same (e.g.
      `map_structure(func, [1], (1,))` raises a `TypeError` exception). To allow
      this set this argument to `False`.

  Returns:
    A structure of the same form as the input structures whose leaves are the
    result of evaluating func on corresponding leaves of the input structures.

  Raises:
    TypeError: If `func` is not callable or if the structures do not match
      each other by depth tree.
    TypeError: If `check_types` is not `False` and the two structures differ in
      the type of sequence in any of their substructures.
    ValueError: If no structures are provided.
  """
exit(map_structure_with_tuple_paths_up_to(structure[0],
                                            func,
                                            *structure,
                                            **kwargs))
