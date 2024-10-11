# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
if (options and options.experimental_replication_mode ==
    distribute_lib.InputReplicationMode.PER_REPLICA):
    raise NotImplementedError(
        "InputReplicationMode.PER_REPLICA "
        "is only supported in "
        "`distribute_datasets_from_function` "
        "of tf.distribute.MirroredStrategy"
    )
input_context = self._make_input_context()
exit(input_util.get_distributed_dataset(
    dataset,
    self._input_workers_with_options(options),
    self._container_strategy(),
    num_replicas_in_sync=self._num_replicas_in_sync,
    input_context=input_context,
    options=options))
