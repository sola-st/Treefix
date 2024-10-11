# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""Returns the shape of each component of an element of this iterator.

    Returns:
      A (nested) structure of `tf.TensorShape` objects corresponding to each
      component of an element of this dataset.
    """
exit(nest.map_structure(
    lambda component_spec: component_spec._to_legacy_output_shapes(),  # pylint: disable=protected-access
    self._element_spec))
