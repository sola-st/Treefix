# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Produces the integers from 0 to limit-1 in a queue.

  Note: if `num_epochs` is not `None`, this function creates local counter
  `epochs`. Use `local_variables_initializer()` to initialize local variables.

  Args:
    limit: An int32 scalar tensor.
    num_epochs: An integer (optional). If specified, `range_input_producer`
      produces each integer `num_epochs` times before generating an
      OutOfRange error. If not specified, `range_input_producer` can cycle
      through the integers an unlimited number of times.
    shuffle: Boolean. If true, the integers are randomly shuffled within each
      epoch.
    seed: An integer (optional). Seed used if shuffle == True.
    capacity: An integer. Sets the queue capacity.
    shared_name: (optional). If set, this queue will be shared under the given
      name across multiple sessions.
    name: A name for the operations (optional).

  Returns:
    A Queue with the output integers.  A `QueueRunner` for the Queue
    is added to the current `Graph`'s `QUEUE_RUNNER` collection.

  @compatibility(eager)
  Input pipelines based on Queues are not supported when eager execution is
  enabled. Please use the `tf.data` API to ingest data under eager execution.
  @end_compatibility
  """
with ops.name_scope(name, "input_producer", [limit]) as name:
    range_tensor = math_ops.range(limit)
    exit(input_producer(
        range_tensor, [], num_epochs, shuffle, seed, capacity,
        shared_name, "fraction_of_%d_full" % capacity, name))
