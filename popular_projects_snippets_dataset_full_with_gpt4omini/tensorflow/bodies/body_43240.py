# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Creates a new structure by applying `func` to each atom in `structure`.

  Refer to [tf.nest](https://www.tensorflow.org/api_docs/python/tf/nest)
  for the definition of a structure.

  Applies `func(x[0], x[1], ...)` where x[i] enumerates all atoms in
  `structure[i]`.  All items in `structure` must have the same arity,
  and the return value will contain results with the same structure layout.

  Examples:

  * A single Python dict:

  >>> a = {"hello": 24, "world": 76}
  >>> tf.nest.map_structure(lambda p: p * 2, a)
  {'hello': 48, 'world': 152}

  * Multiple Python dictionaries:

  >>> d1 = {"hello": 24, "world": 76}
  >>> d2 = {"hello": 36, "world": 14}
  >>> tf.nest.map_structure(lambda p1, p2: p1 + p2, d1, d2)
  {'hello': 60, 'world': 90}

  * A single Python list:

  >>> a = [24, 76, "ab"]
  >>> tf.nest.map_structure(lambda p: p * 2, a)
  [48, 152, 'abab']

  * Scalars:

  >>> tf.nest.map_structure(lambda x, y: x + y, 3, 4)
  7

  * Empty structures:

  >>> tf.nest.map_structure(lambda x: x + 1, ())
  ()

  * Check the types of iterables:

  >>> s1 = (((1, 2), 3), 4, (5, 6))
  >>> s1_list = [[[1, 2], 3], 4, [5, 6]]
  >>> tf.nest.map_structure(lambda x, y: None, s1, s1_list)
  Traceback (most recent call last):
  ...
  TypeError: The two structures don't have the same nested structure

  * Type check is set to False:

  >>> s1 = (((1, 2), 3), 4, (5, 6))
  >>> s1_list = [[[1, 2], 3], 4, [5, 6]]
  >>> tf.nest.map_structure(lambda x, y: None, s1, s1_list, check_types=False)
  (((None, None), None), None, (None, None))

  Args:
    func: A callable that accepts as many arguments as there are structures.
    *structure: atom or nested structure.
    **kwargs: Valid keyword args are:
      * `check_types`: If set to `True` (default) the types of iterables within
        the structures have to be same (e.g. `map_structure(func, [1], (1,))`
        raises a `TypeError` exception). To allow this set this argument to
        `False`. Note that namedtuples with identical name and fields are always
        considered to have the same shallow structure.
      * `expand_composites`: If set to `True`, then composite tensors such as
        `tf.sparse.SparseTensor` and `tf.RaggedTensor` are expanded into their
        component tensors.  If `False` (the default), then composite tensors are
        not expanded.

  Returns:
    A new structure with the same arity as `structure[0]`, whose atoms
    correspond to `func(x[0], x[1], ...)` where `x[i]` is the atom in the
    corresponding location in `structure[i]`. If there are different structure
    types and `check_types` is `False` the structure types of the first
    structure will be used.

  Raises:
    TypeError: If `func` is not callable or if the structures do not match
      each other by depth tree.
    ValueError: If no structure is provided or if the structures do not match
      each other by type.
    ValueError: If wrong keyword arguments are provided.
  """
if not callable(func):
    raise TypeError("func must be callable, got: %s" % func)

if not structure:
    raise ValueError("Must provide at least one structure")

check_types = kwargs.pop("check_types", True)
expand_composites = kwargs.pop("expand_composites", False)

if kwargs:
    raise ValueError(
        "Only valid keyword arguments are `check_types` and "
        "`expand_composites`, not: `%s`" % ("`, `".join(kwargs.keys())))

for other in structure[1:]:
    assert_same_structure(structure[0], other, check_types=check_types,
                          expand_composites=expand_composites)

flat_structure = (flatten(s, expand_composites) for s in structure)
entries = zip(*flat_structure)

exit(pack_sequence_as(
    structure[0], [func(*x) for x in entries],
    expand_composites=expand_composites))
