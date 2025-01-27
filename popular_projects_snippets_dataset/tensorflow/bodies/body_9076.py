# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Create dataset on each worker.

    This creates dataset on workers from the input which can be either a
    `tf.data.Dataset`, a `tf.distribute.DistributedDataset` or a function which
    returns a dataset, and returns an object that represents the collection of
    those individual datasets. Calling `iter` on such collection of datasets
    returns a `tf.distribute.experimental.coordinator.PerWorkerValues`, which is
    a collection of iterators, where the iterators have been placed on
    respective workers.

    Calling `next` on a `PerWorkerValues` of iterator is unsupported. The
    iterator is meant to be passed as an argument into
    `tf.distribute.experimental.coordinator.ClusterCoordinator.schedule`. When
    the scheduled function is about to be executed by a worker, the
    function will receive the individual iterator that corresponds to the
    worker. The `next` method can be called on an iterator inside a
    scheduled function when the iterator is an input of the function.

    Currently the `schedule` method assumes workers are all the same and thus
    assumes the datasets on different workers are the same, except they may be
    shuffled differently if they contain a `dataset.shuffle` operation and a
    random seed is not set. Because of this, we also recommend the datasets to
    be repeated indefinitely and schedule a finite number of steps instead of
    relying on the `OutOfRangeError` from a dataset.


    Example:

    ```python
    strategy = tf.distribute.experimental.ParameterServerStrategy(
        cluster_resolver=...)
    coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
        strategy=strategy)

    @tf.function
    def worker_fn(iterator):
      return next(iterator)

    def per_worker_dataset_fn():
      return strategy.distribute_datasets_from_function(
          lambda x: tf.data.Dataset.from_tensor_slices([3] * 3))

    per_worker_dataset = coordinator.create_per_worker_dataset(
        per_worker_dataset_fn)
    per_worker_iter = iter(per_worker_dataset)
    remote_value = coordinator.schedule(worker_fn, args=(per_worker_iter,))
    assert remote_value.fetch() == 3
    ```

    Args:
      dataset_fn: The dataset function that returns a dataset. This is to be
        executed on the workers.

    Returns:
      An object that represents the collection of those individual
      datasets. `iter` is expected to be called on this object that returns
      a `tf.distribute.experimental.coordinator.PerWorkerValues` of the
      iterators (that are on the workers).
    """
exit(values_lib.get_per_worker_dataset(dataset_fn, self))
