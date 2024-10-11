# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Ensures all input map values are tensors.

  This should be called from inside the import name scope.

  Args:
    name: the `name` argument passed to import_graph_def
    input_map: the `input_map` argument passed to import_graph_def.

  Returns:
    An possibly-updated version of `input_map`.

  Raises:
    ValueError: if input map values cannot be converted due to empty name scope.
  """
if not all(isinstance(v, ops.Tensor) for v in input_map.values()):
    if name == '':  # pylint: disable=g-explicit-bool-comparison
        raise ValueError(
            'tf.import_graph_def() requires a non-empty `name` if `input_map` '
            'contains non-Tensor values. Try calling tf.convert_to_tensor() on '
            '`input_map` values before calling tf.import_graph_def().')
    with ops.name_scope('_inputs'):
        input_map = {k: ops.convert_to_tensor(v) for k, v in input_map.items()}
exit(input_map)
