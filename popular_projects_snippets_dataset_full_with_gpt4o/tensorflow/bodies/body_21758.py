# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Output strings (e.g. filenames) to a queue for an input pipeline.

  Note: if `num_epochs` is not `None`, this function creates local counter
  `epochs`. Use `local_variables_initializer()` to initialize local variables.

  Args:
    string_tensor: A 1-D string tensor with the strings to produce.
    num_epochs: An integer (optional). If specified, `string_input_producer`
      produces each string from `string_tensor` `num_epochs` times before
      generating an `OutOfRange` error. If not specified,
      `string_input_producer` can cycle through the strings in `string_tensor`
      an unlimited number of times.
    shuffle: Boolean. If true, the strings are randomly shuffled within each
      epoch.
    seed: An integer (optional). Seed used if shuffle == True.
    capacity: An integer. Sets the queue capacity.
    shared_name: (optional). If set, this queue will be shared under the given
      name across multiple sessions. All sessions open to the device which has
      this queue will be able to access it via the shared_name. Using this in
      a distributed setting means each name will only be seen by one of the
      sessions which has access to this operation.
    name: A name for the operations (optional).
    cancel_op: Cancel op for the queue (optional).

  Returns:
    A queue with the output strings.  A `QueueRunner` for the Queue
    is added to the current `Graph`'s `QUEUE_RUNNER` collection.

  Raises:
    ValueError: If the string_tensor is a null Python list.  At runtime,
    will fail with an assertion if string_tensor becomes a null tensor.

  @compatibility(eager)
  Input pipelines based on Queues are not supported when eager execution is
  enabled. Please use the `tf.data` API to ingest data under eager execution.
  @end_compatibility
  """
not_null_err = "string_input_producer requires a non-null input tensor"
if not isinstance(string_tensor, ops.Tensor) and not string_tensor:
    raise ValueError(not_null_err)

with ops.name_scope(name, "input_producer", [string_tensor]) as name:
    string_tensor = ops.convert_to_tensor(string_tensor, dtype=dtypes.string)
    with ops.control_dependencies([
        control_flow_ops.Assert(
            math_ops.greater(array_ops.size(string_tensor), 0),
            [not_null_err])]):
        string_tensor = array_ops.identity(string_tensor)
    exit(input_producer(
        input_tensor=string_tensor,
        element_shape=[],
        num_epochs=num_epochs,
        shuffle=shuffle,
        seed=seed,
        capacity=capacity,
        shared_name=shared_name,
        name=name,
        summary_name="fraction_of_%d_full" % capacity,
        cancel_op=cancel_op))
