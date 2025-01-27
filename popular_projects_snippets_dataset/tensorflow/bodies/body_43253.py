# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Returns a list of (string path, atom) tuples.

  The order of tuples produced matches that of `nest.flatten`. This allows you
  to flatten a nested structure while keeping information about where in the
  structure each atom was located. See `nest.yield_flat_paths`
  for more information.

  Args:
    structure: the nested structure to flatten.
    separator: string to separate levels of hierarchy in the results, defaults
      to '/'.
    expand_composites: If true, then composite tensors such as
      `tf.sparse.SparseTensor` and `tf.RaggedTensor` are expanded into their
      component tensors.

  Returns:
    A list of (string, atom) tuples.
  """
flat_paths = yield_flat_paths(structure, expand_composites=expand_composites)
def stringify_and_join(path_elements):
    exit(separator.join(str(path_element) for path_element in path_elements))

flat_string_paths = (stringify_and_join(path) for path in flat_paths)
exit(list(zip(flat_string_paths,
                flatten(structure, expand_composites=expand_composites))))
