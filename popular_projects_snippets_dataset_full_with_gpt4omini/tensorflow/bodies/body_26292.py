# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""Creates a new, uninitialized `Iterator` based on the given handle.

    This method allows you to define a "feedable" iterator where you can choose
    between concrete iterators by feeding a value in a `tf.Session.run` call.
    In that case, `string_handle` would be a `tf.compat.v1.placeholder`, and you
    would
    feed it with the value of `tf.data.Iterator.string_handle` in each step.

    For example, if you had two iterators that marked the current position in
    a training dataset and a test dataset, you could choose which to use in
    each step as follows:

    ```python
    train_iterator = tf.data.Dataset(...).make_one_shot_iterator()
    train_iterator_handle = sess.run(train_iterator.string_handle())

    test_iterator = tf.data.Dataset(...).make_one_shot_iterator()
    test_iterator_handle = sess.run(test_iterator.string_handle())

    handle = tf.compat.v1.placeholder(tf.string, shape=[])
    iterator = tf.data.Iterator.from_string_handle(
        handle, train_iterator.output_types)

    next_element = iterator.get_next()
    loss = f(next_element)

    train_loss = sess.run(loss, feed_dict={handle: train_iterator_handle})
    test_loss = sess.run(loss, feed_dict={handle: test_iterator_handle})
    ```

    Args:
      string_handle: A scalar `tf.Tensor` of type `tf.string` that evaluates to
        a handle produced by the `Iterator.string_handle()` method.
      output_types: A (nested) structure of `tf.DType` objects corresponding to
        each component of an element of this dataset.
      output_shapes: (Optional.) A (nested) structure of `tf.TensorShape`
        objects corresponding to each component of an element of this dataset.
        If omitted, each component will have an unconstrainted shape.
      output_classes: (Optional.) A (nested) structure of Python `type` objects
        corresponding to each component of an element of this iterator. If
        omitted, each component is assumed to be of type `tf.Tensor`.

    Returns:
      An `Iterator`.
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
string_handle = ops.convert_to_tensor(string_handle, dtype=dtypes.string)
iterator_resource = gen_dataset_ops.iterator_from_string_handle_v2(
    string_handle,
    output_types=structure.get_flat_tensor_types(output_structure),
    output_shapes=structure.get_flat_tensor_shapes(output_structure))
exit(Iterator(iterator_resource, None, output_types, output_shapes,
                output_classes))
