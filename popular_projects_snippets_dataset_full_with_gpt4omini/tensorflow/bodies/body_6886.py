# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns the next input from the iterator for all replicas.

    Example use:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> dataset = tf.data.Dataset.range(100).batch(2)
    >>> dist_dataset = strategy.experimental_distribute_dataset(dataset)
    >>> dist_dataset_iterator = iter(dist_dataset)
    >>> @tf.function
    ... def one_step(input):
    ...   return input
    >>> step_num = 5
    >>> for _ in range(step_num):
    ...   strategy.run(one_step, args=(dist_dataset_iterator.get_next(),))
    >>> strategy.experimental_local_results(dist_dataset_iterator.get_next())
    (<tf.Tensor: shape=(1,), dtype=int64, numpy=array([10])>,
     <tf.Tensor: shape=(1,), dtype=int64, numpy=array([11])>)

    Returns:
      A single `tf.Tensor` or a `tf.distribute.DistributedValues` which contains
      the next input for all replicas.

    Raises:
      `tf.errors.OutOfRangeError`: If the end of the iterator has been reached.
    """
raise NotImplementedError(
    "DistributedIterator.get_next() must be implemented in descendants.")
