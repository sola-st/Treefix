# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
# Note that split_batch_by argument is not passed because it is always 1 in
# this strategy, and adding it adds unnecessary overhead to the dataset.
if (options and options.experimental_replication_mode ==
    distribute_lib.InputReplicationMode.PER_REPLICA):
    raise NotImplementedError(
        "InputReplicationMode.PER_REPLICA "
        "is only supported in  "
        "`experimental_distribute_datasets_from_function`."
    )
exit(input_util.get_distributed_dataset(
    dataset,
    self._input_workers_with_options(options),
    self._container_strategy(),
    options=options))
