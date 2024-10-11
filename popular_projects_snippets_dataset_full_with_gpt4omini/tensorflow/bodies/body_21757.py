# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Output the rows of `input_tensor` to a queue for an input pipeline.

  Note: if `num_epochs` is not `None`, this function creates local counter
  `epochs`. Use `local_variables_initializer()` to initialize local variables.

  Args:
    input_tensor: A tensor with the rows to produce. Must be at least
      one-dimensional. Must either have a fully-defined shape, or
      `element_shape` must be defined.
    element_shape: (Optional.) A `TensorShape` representing the shape of a
      row of `input_tensor`, if it cannot be inferred.
    num_epochs: (Optional.) An integer. If specified `input_producer` produces
      each row of `input_tensor` `num_epochs` times before generating an
      `OutOfRange` error. If not specified, `input_producer` can cycle through
      the rows of `input_tensor` an unlimited number of times.
    shuffle: (Optional.) A boolean. If true, the rows are randomly shuffled
      within each epoch.
    seed: (Optional.) An integer. The seed to use if `shuffle` is true.
    capacity: (Optional.) The capacity of the queue to be used for buffering
      the input.
    shared_name: (Optional.) If set, this queue will be shared under the given
      name across multiple sessions.
    summary_name: (Optional.) If set, a scalar summary for the current queue
      size will be generated, using this name as part of the tag.
    name: (Optional.) A name for queue.
    cancel_op: (Optional.) Cancel op for the queue

  Returns:
    A queue with the output rows.  A `QueueRunner` for the queue is
    added to the current `QUEUE_RUNNER` collection of the current
    graph.

  Raises:
    ValueError: If the shape of the input cannot be inferred from the arguments.
    RuntimeError: If called with eager execution enabled.

  @compatibility(eager)
  Input pipelines based on Queues are not supported when eager execution is
  enabled. Please use the `tf.data` API to ingest data under eager execution.
  @end_compatibility
  """
if context.executing_eagerly():
    raise RuntimeError(
        "Input pipelines based on Queues are not supported when eager execution"
        " is enabled. Please use tf.data to ingest data into your model"
        " instead.")
with ops.name_scope(name, "input_producer", [input_tensor]):
    input_tensor = ops.convert_to_tensor(input_tensor, name="input_tensor")
    element_shape = input_tensor.shape[1:].merge_with(element_shape)
    if not element_shape.is_fully_defined():
        raise ValueError("Either `input_tensor` must have a fully defined shape "
                         "or `element_shape` must be specified")

    if shuffle:
        input_tensor = random_ops.random_shuffle(input_tensor, seed=seed)

    input_tensor = limit_epochs(input_tensor, num_epochs)

    q = data_flow_ops.FIFOQueue(capacity=capacity,
                                dtypes=[input_tensor.dtype.base_dtype],
                                shapes=[element_shape],
                                shared_name=shared_name, name=name)
    enq = q.enqueue_many([input_tensor])
    queue_runner.add_queue_runner(
        queue_runner.QueueRunner(
            q, [enq], cancel_op=cancel_op))
    if summary_name is not None:
        summary.scalar(summary_name,
                       math_ops.cast(q.size(), dtypes.float32) * (1. / capacity))
    exit(q)
