# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if (options and options.experimental_replication_mode ==
    distribute_lib.InputReplicationMode.PER_REPLICA):
    raise NotImplementedError(
        "InputReplicationMode.PER_REPLICA "
        "is only supported in "
        "`experimental_distribute_datasets_from_function`."
    )
if options is None or options.experimental_fetch_to_device:
    self._check_spec(dataset.element_spec)

exit(input_util.get_distributed_dataset(
    dataset,
    self._get_input_workers(options),
    self._container_strategy(),
    num_replicas_in_sync=self._num_replicas_in_sync,
    options=options))
