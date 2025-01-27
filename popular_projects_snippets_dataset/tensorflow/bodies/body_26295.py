# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
"""Returns the next element.

    In graph mode, you should typically call this method *once* and use its
    result as the input to another computation. A typical loop will then call
    `tf.Session.run` on the result of that computation. The loop will terminate
    when the `Iterator.get_next()` operation raises
    `tf.errors.OutOfRangeError`. The following skeleton shows how to use
    this method when building a training loop:

    ```python
    dataset = ...  # A `tf.data.Dataset` object.
    iterator = dataset.make_initializable_iterator()
    next_element = iterator.get_next()

    # Build a TensorFlow graph that does something with each element.
    loss = model_function(next_element)
    optimizer = ...  # A `tf.compat.v1.train.Optimizer` object.
    train_op = optimizer.minimize(loss)

    with tf.compat.v1.Session() as sess:
      try:
        while True:
          sess.run(train_op)
      except tf.errors.OutOfRangeError:
        pass
    ```

    NOTE: It is legitimate to call `Iterator.get_next()` multiple times, e.g.
    when you are distributing different elements to multiple devices in a single
    step. However, a common pitfall arises when users call `Iterator.get_next()`
    in each iteration of their training loop. `Iterator.get_next()` adds ops to
    the graph, and executing each op allocates resources (including threads); as
    a consequence, invoking it in every iteration of a training loop causes
    slowdown and eventual resource exhaustion. To guard against this outcome, we
    log a warning when the number of uses crosses a fixed threshold of
    suspiciousness.

    Args:
      name: (Optional.) A name for the created operation.

    Returns:
      A (nested) structure of values matching `tf.data.Iterator.element_spec`.
    """
self._get_next_call_count += 1
if self._get_next_call_count > GET_NEXT_CALL_WARNING_THRESHOLD:
    warnings.warn(GET_NEXT_CALL_WARNING_MESSAGE)

# TODO(b/169442955): Investigate the need for this colocation constraint.
with ops.colocate_with(self._iterator_resource):
    # pylint: disable=protected-access
    flat_ret = gen_dataset_ops.iterator_get_next(
        self._iterator_resource,
        output_types=self._flat_tensor_types,
        output_shapes=self._flat_tensor_shapes,
        name=name)
    exit(structure.from_tensor_list(self._element_spec, flat_ret))
