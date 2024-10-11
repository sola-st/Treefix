# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
# pylint: disable=line-too-long
"""Distributes `tf.data.Dataset` instances created by calls to `dataset_fn`.

    The argument `dataset_fn` that users pass in is an input function that has a
    `tf.distribute.InputContext` argument and returns a `tf.data.Dataset`
    instance. It is expected that the returned dataset from `dataset_fn` is
    already batched by per-replica batch size (i.e. global batch size divided by
    the number of replicas in sync) and sharded.
    `tf.distribute.Strategy.distribute_datasets_from_function` does
    not batch or shard the `tf.data.Dataset` instance
    returned from the input function. `dataset_fn` will be called on the CPU
    device of each of the workers and each generates a dataset where every
    replica on that worker will dequeue one batch of inputs (i.e. if a worker
    has two replicas, two batches will be dequeued from the `Dataset` every
    step).

    This method can be used for several purposes. First, it allows you to
    specify your own batching and sharding logic. (In contrast,
    `tf.distribute.experimental_distribute_dataset` does batching and sharding
    for you.) For example, where
    `experimental_distribute_dataset` is unable to shard the input files, this
    method might be used to manually shard the dataset (avoiding the slow
    fallback behavior in `experimental_distribute_dataset`). In cases where the
    dataset is infinite, this sharding can be done by creating dataset replicas
    that differ only in their random seed.

    The `dataset_fn` should take an `tf.distribute.InputContext` instance where
    information about batching and input replication can be accessed.

    You can use `element_spec` property of the
    `tf.distribute.DistributedDataset` returned by this API to query the
    `tf.TypeSpec` of the elements returned by the iterator. This can be used to
    set the `input_signature` property of a `tf.function`. Follow
    `tf.distribute.DistributedDataset.element_spec` to see an example.

    IMPORTANT: The `tf.data.Dataset` returned by `dataset_fn` should have a
    per-replica batch size, unlike `experimental_distribute_dataset`, which uses
    the global batch size. This may be computed using
    `input_context.get_per_replica_batch_size`.

    Note: If you are using TPUStrategy, the order in which the data is processed
    by the workers when using
    `tf.distribute.Strategy.experimental_distribute_dataset` or
    `tf.distribute.Strategy.distribute_datasets_from_function` is
    not guaranteed. This is typically required if you are using
    `tf.distribute` to scale prediction. You can however insert an index for
    each element in the batch and order outputs accordingly. Refer to [this
    snippet](https://www.tensorflow.org/tutorials/distribute/input#caveats)
    for an example of how to order outputs.

    Note: Stateful dataset transformations are currently not supported with
    `tf.distribute.experimental_distribute_dataset` or
    `tf.distribute.distribute_datasets_from_function`. Any stateful
    ops that the dataset may have are currently ignored. For example, if your
    dataset has a `map_fn` that uses `tf.random.uniform` to rotate an image,
    then you have a dataset graph that depends on state (i.e the random seed) on
    the local machine where the python process is being executed.

    For a tutorial on more usage and properties of this method, refer to the
    [tutorial on distributed input](https://www.tensorflow.org/tutorials/distribute/input#tfdistributestrategyexperimental_distribute_datasets_from_function)).
    If you are interested in last partial batch handling, read [this section](https://www.tensorflow.org/tutorials/distribute/input#partial_batches).

    Args:
      dataset_fn: A function taking a `tf.distribute.InputContext` instance and
        returning a `tf.data.Dataset`.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.

    Returns:
      A `tf.distribute.DistributedDataset`.
    """
distribution_strategy_input_api_counter.get_cell(
    self.__class__.__name__,
    "distribute_datasets_from_function").increase_by(1)
# pylint: enable=line-too-long
exit(self._extended._distribute_datasets_from_function(  # pylint: disable=protected-access
    dataset_fn, options))
