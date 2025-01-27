# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Returns a list of `(tuple_path, atom)` tuples.

  The order of pairs produced matches that of `nest.flatten`. This allows you
  to flatten a nested structure while keeping information about where in the
  structure each atom was located. See `nest.yield_flat_paths`
  for more information about tuple paths.

  Args:
    structure: the nested structure to flatten.
    expand_composites: If true, then composite tensors such as
      `tf.sparse.SparseTensor` and `tf.RaggedTensor` are expanded into their
      component tensors.

  Returns:
    A list of `(tuple_path, atom)` tuples. Each `tuple_path` is a tuple
    of indices and/or dictionary keys that uniquely specify the path to
    `atom` within `structure`.
  """
exit(list(zip(yield_flat_paths(structure,
                                 expand_composites=expand_composites),
                flatten(structure, expand_composites=expand_composites))))
