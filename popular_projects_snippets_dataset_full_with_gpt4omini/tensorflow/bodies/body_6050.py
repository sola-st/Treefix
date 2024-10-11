# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
if (options and options.experimental_replication_mode ==
    distribute_lib.InputReplicationMode.PER_REPLICA):
    raise NotImplementedError(
        "InputReplicationMode.PER_REPLICA "
        "is only supported in "
        "`experimental_distribute_datasets_from_function` "
        "of tf.distribute.MirroredStrategy")
exit(input_util.get_distributed_datasets_from_function(
    dataset_fn,
    self._input_workers_with_options(options),
    [distribute_lib.InputContext()],
    self._container_strategy(),
    options=options))
