# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# pylint: disable=line-too-long
"""The type specification of an element of `tf.distribute.DistributedIterator`.

    Example usage:

    >>> global_batch_size = 16
    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> dataset = tf.data.Dataset.from_tensors(([1.],[2])).repeat(100).batch(global_batch_size)
    >>> distributed_iterator = iter(strategy.experimental_distribute_dataset(dataset))
    >>> distributed_iterator.element_spec
    (PerReplicaSpec(TensorSpec(shape=(None, 1), dtype=tf.float32, name=None),
                    TensorSpec(shape=(None, 1), dtype=tf.float32, name=None)),
     PerReplicaSpec(TensorSpec(shape=(None, 1), dtype=tf.int32, name=None),
                    TensorSpec(shape=(None, 1), dtype=tf.int32, name=None)))

    Returns:
      A nested structure of `tf.TypeSpec` objects matching the structure of an
      element of this `tf.distribute.DistributedIterator`. This returned value
      is typically a `tf.distribute.DistributedValues` object and specifies the
      `tf.TensorSpec` of individual components.
    """
raise NotImplementedError(
    "DistributedIterator.element_spec() must be implemented in descendants")
