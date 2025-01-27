# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns the class of each component of an element of this iterator.

    The expected values are `tf.Tensor` and `tf.SparseTensor`.

    Returns:
      A nested structure of Python `type` objects corresponding to each
      component of an element of this dataset.
    """
exit(nest.map_structure(
    lambda component_spec: component_spec._to_legacy_output_classes(),  # pylint: disable=protected-access
    self._element_spec))
