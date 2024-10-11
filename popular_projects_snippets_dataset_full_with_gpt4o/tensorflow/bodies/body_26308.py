# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""Creates a new iterator from the given dataset.

    If `dataset` is not specified, the iterator will be created from the given
    tensor components and element structure. In particular, the alternative for
    constructing the iterator is used when the iterator is reconstructed from
    it `CompositeTensor` representation.

    Args:
      dataset: A `tf.data.Dataset` object.
      components: Tensor components to construct the iterator from.
      element_spec: A (nested) structure of `TypeSpec` objects that
        represents the type specification of elements of the iterator.

    Raises:
      ValueError: If `dataset` is not provided and either `components` or
        `element_spec` is not provided. Or `dataset` is provided and either
        `components` and `element_spec` is provided.
    """
super(OwnedIterator, self).__init__()

if dataset is None:
    if (components is None or element_spec is None):
        raise ValueError(
            "When `dataset` is not provided, both `components` and "
            "`element_spec` must be specified.")
    # pylint: disable=protected-access
    self._element_spec = element_spec
    self._flat_output_types = structure.get_flat_tensor_types(
        self._element_spec)
    self._flat_output_shapes = structure.get_flat_tensor_shapes(
        self._element_spec)
    self._iterator_resource, = components
else:
    if (components is not None or element_spec is not None):
        raise ValueError(
            "When `dataset` is provided, `element_spec` and `components` must "
            "not be specified.")
    self._create_iterator(dataset)

self._get_next_call_count = 0
