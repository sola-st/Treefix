# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
"""Make an iterator for input provided via an input function.

    Currently implements PER_WORKER mode, in which the `input_fn` is called
    once on each worker.

    TODO(priyag): Add other replication modes.

    Args:
      input_fn: Input function that returns a `tf.data.Dataset` object.
      input_workers: an `InputWorkers` object.
      input_contexts: A list of `InputContext` instances to be passed to call(s)
        to `input_fn`. Length and order should match worker order in
        `worker_device_pairs`.
      strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
        handle last partial batch.
    """
assert isinstance(input_workers, input_lib.InputWorkers)
if input_workers.num_workers != len(input_contexts):
    raise ValueError("Number of input workers (%d) is not same as number of "
                     "input_contexts (%d)" %
                     (input_workers.num_workers, len(input_contexts)))

iterators = []
for i, ctx in enumerate(input_contexts):
    worker = input_workers.worker_devices[i]
    with ops.device(worker):
        result = input_fn(ctx)
        devices = input_workers.compute_devices_for_worker(i)
        if isinstance(result, dataset_ops.DatasetV2):
            iterator = _SingleWorkerDatasetIterator(result, worker, devices)
        elif callable(result):
            iterator = _SingleWorkerCallableIterator(result, worker, devices)
        else:
            raise ValueError(
                "input_fn must return a tf.data.Dataset or a callable.")
        iterators.append(iterator)

super(InputFunctionIterator, self).__init__(
    input_workers,
    iterators,
    strategy,
    cardinality=cardinality_lib.UNKNOWN,
    enable_get_next_as_optional=False)
self._enable_get_next_as_optional = False
