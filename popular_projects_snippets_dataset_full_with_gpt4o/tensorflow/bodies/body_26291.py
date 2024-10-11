# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""Creates a new, uninitialized `Iterator` with the given structure.

    This iterator-constructing method can be used to create an iterator that
    is reusable with many different datasets.

    The returned iterator is not bound to a particular dataset, and it has
    no `initializer`. To initialize the iterator, run the operation returned by
    `Iterator.make_initializer(dataset)`.

    The following is an example

    ```python
    iterator = Iterator.from_structure(tf.int64, tf.TensorShape([]))

    dataset_range = Dataset.range(10)
    range_initializer = iterator.make_initializer(dataset_range)

    dataset_evens = dataset_range.filter(lambda x: x % 2 == 0)
    evens_initializer = iterator.make_initializer(dataset_evens)

    # Define a model based on the iterator; in this example, the model_fn
    # is expected to take scalar tf.int64 Tensors as input (see
    # the definition of 'iterator' above).
    prediction, loss = model_fn(iterator.get_next())

    # Train for `num_epochs`, where for each epoch, we first iterate over
    # dataset_range, and then iterate over dataset_evens.
    for _ in range(num_epochs):
      # Initialize the iterator to `dataset_range`
      sess.run(range_initializer)
      while True:
        try:
          pred, loss_val = sess.run([prediction, loss])
        except tf.errors.OutOfRangeError:
          break

      # Initialize the iterator to `dataset_evens`
      sess.run(evens_initializer)
      while True:
        try:
          pred, loss_val = sess.run([prediction, loss])
        except tf.errors.OutOfRangeError:
          break
    ```

    Args:
      output_types: A (nested) structure of `tf.DType` objects corresponding to
        each component of an element of this dataset.
      output_shapes: (Optional.) A (nested) structure of `tf.TensorShape`
        objects corresponding to each component of an element of this dataset.
        If omitted, each component will have an unconstrainted shape.
      shared_name: (Optional.) If non-empty, this iterator will be shared under
        the given name across multiple sessions that share the same devices
        (e.g. when using a remote server).
      output_classes: (Optional.) A (nested) structure of Python `type` objects
        corresponding to each component of an element of this iterator. If
        omitted, each component is assumed to be of type `tf.Tensor`.

    Returns:
      An `Iterator`.

    Raises:
      TypeError: If the structures of `output_shapes` and `output_types` are
        not the same.
    """
output_types = nest.map_structure(dtypes.as_dtype, output_types)
if output_shapes is None:
    output_shapes = nest.map_structure(
        lambda _: tensor_shape.TensorShape(None), output_types)
else:
    output_shapes = nest.map_structure_up_to(output_types,
                                             tensor_shape.as_shape,
                                             output_shapes)
if output_classes is None:
    output_classes = nest.map_structure(lambda _: ops.Tensor, output_types)
nest.assert_same_structure(output_types, output_shapes)
output_structure = structure.convert_legacy_structure(
    output_types, output_shapes, output_classes)
if shared_name is None:
    shared_name = ""
iterator_resource = gen_dataset_ops.iterator_v2(
    container="",
    shared_name=shared_name,
    output_types=structure.get_flat_tensor_types(output_structure),
    output_shapes=structure.get_flat_tensor_shapes(
        output_structure))
exit(Iterator(iterator_resource, None, output_types, output_shapes,
                output_classes))
