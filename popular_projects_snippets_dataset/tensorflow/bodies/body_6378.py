# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
if (options and options.experimental_replication_mode ==
    distribute_lib.InputReplicationMode.PER_REPLICA):
    raise NotImplementedError(
        "InputReplicationMode.PER_REPLICA "
        "is only supported in "
        "`distribute_datasets_from_function` "
        "of tf.distribute.MirroredStrategy")
input_context = self._make_input_context()
exit(input_util.get_distributed_datasets_from_function(
    dataset_fn=dataset_fn,
    input_workers=self._input_workers_with_options(options),
    input_contexts=[input_context],
    strategy=self._container_strategy(),
    options=options))
