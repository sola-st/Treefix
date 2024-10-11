# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""Returns a `tf.Operation` that initializes this iterator on `dataset`.

    Args:
      dataset: A `Dataset` whose `element_spec` if compatible with this
        iterator.
      name: (Optional.) A name for the created operation.

    Returns:
      A `tf.Operation` that can be run to initialize this iterator on the given
      `dataset`.

    Raises:
      TypeError: If `dataset` and this iterator do not have a compatible
        `element_spec`.
    """
with ops.name_scope(name, "make_initializer") as name:
    # NOTE(mrry): Cannot depend on `dataset_ops.get_legacy_output*()` due
    # to that creating a circular dependency.
    # pylint: disable=protected-access
    dataset_output_types = nest.map_structure(
        lambda component_spec: component_spec._to_legacy_output_types(),
        dataset.element_spec)
    dataset_output_shapes = nest.map_structure(
        lambda component_spec: component_spec._to_legacy_output_shapes(),
        dataset.element_spec)
    dataset_output_classes = nest.map_structure(
        lambda component_spec: component_spec._to_legacy_output_classes(),
        dataset.element_spec)
    # pylint: enable=protected-access

    nest.assert_same_structure(self.output_types, dataset_output_types)
    nest.assert_same_structure(self.output_shapes, dataset_output_shapes)
    for iterator_class, dataset_class in zip(
        nest.flatten(self.output_classes),
        nest.flatten(dataset_output_classes)):
        if iterator_class is not dataset_class:
            raise TypeError(
                f"Expected output classes {self.output_classes!r} but got "
                f"dataset with output classes {dataset_output_classes!r}.")
    for iterator_dtype, dataset_dtype in zip(
        nest.flatten(self.output_types), nest.flatten(dataset_output_types)):
        if iterator_dtype != dataset_dtype:
            raise TypeError(
                f"Expected output types {self.output_types!r} but got dataset "
                f"with output types {dataset_output_types!r}.")
    for iterator_shape, dataset_shape in zip(
        nest.flatten(self.output_shapes), nest.flatten(
            dataset_output_shapes)):
        if not iterator_shape.is_compatible_with(dataset_shape):
            raise TypeError(
                f"Expected output shapes compatible with {self.output_shapes!r} "
                f"but got dataset with output shapes {dataset_output_shapes!r}.")

    # TODO(b/169442955): Investigate the need for this colocation constraint.
with ops.colocate_with(self._iterator_resource):
    # pylint: disable=protected-access
    exit(gen_dataset_ops.make_iterator(
        dataset._variant_tensor, self._iterator_resource, name=name))
