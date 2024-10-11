# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# pylint: disable=line-too-long
"""Returns a `tf.experimental.Optional` that contains the next value for all replicas.

    If the `tf.distribute.DistributedIterator` has reached the end of the
    sequence, the returned `tf.experimental.Optional` will have no value.

    Example usage:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> global_batch_size = 2
    >>> steps_per_loop = 2
    >>> dataset = tf.data.Dataset.range(10).batch(global_batch_size)
    >>> distributed_iterator = iter(
    ...     strategy.experimental_distribute_dataset(dataset))
    >>> def step_fn(x):
    ...   # train the model with inputs
    ...   return x
    >>> @tf.function
    ... def train_fn(distributed_iterator):
    ...   for _ in tf.range(steps_per_loop):
    ...     optional_data = distributed_iterator.get_next_as_optional()
    ...     if not optional_data.has_value():
    ...       break
    ...     per_replica_results = strategy.run(step_fn, args=(optional_data.get_value(),))
    ...     tf.print(strategy.experimental_local_results(per_replica_results))
    >>> train_fn(distributed_iterator)
    ... # ([0 1], [2 3])
    ... # ([4], [])

    Returns:
      An `tf.experimental.Optional` object representing the next value from the
      `tf.distribute.DistributedIterator` (if it has one) or no value.
    """
# pylint: enable=line-too-long
raise NotImplementedError(
    "get_next_as_optional() not implemented in descendants")
