# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""Creates a new iterator from the given iterator resource.

    Note: Most users will not call this initializer directly, and will
    instead use `Dataset.make_initializable_iterator()` or
    `Dataset.make_one_shot_iterator()`.

    Args:
      iterator_resource: A `tf.resource` scalar `tf.Tensor` representing the
        iterator.
      initializer: A `tf.Operation` that should be run to initialize this
        iterator.
      output_types: A (nested) structure of `tf.DType` objects corresponding to
        each component of an element of this iterator.
      output_shapes: A (nested) structure of `tf.TensorShape` objects
        corresponding to each component of an element of this iterator.
      output_classes: A (nested) structure of Python `type` objects
        corresponding to each component of an element of this iterator.

    Raises:
      TypeError: If `output_types`, `output_shapes`, or `output_classes` is not
        specified.
    """
self._iterator_resource = iterator_resource
self._initializer = initializer

if (output_types is None or output_shapes is None
    or output_classes is None):
    raise ValueError(
        "All of `output_types`, `output_shapes`, and `output_classes` "
        "must be specified to create an iterator. Got "
        f"`output_types` = {output_types!r}, "
        f"`output_shapes` = {output_shapes!r}, "
        f"`output_classes` = {output_classes!r}.")
self._element_spec = structure.convert_legacy_structure(
    output_types, output_shapes, output_classes)
self._flat_tensor_shapes = structure.get_flat_tensor_shapes(
    self._element_spec)
self._flat_tensor_types = structure.get_flat_tensor_types(
    self._element_spec)

self._string_handle = gen_dataset_ops.iterator_to_string_handle(
    self._iterator_resource)
self._get_next_call_count = 0
ops.add_to_collection(GLOBAL_ITERATORS, self._iterator_resource)
