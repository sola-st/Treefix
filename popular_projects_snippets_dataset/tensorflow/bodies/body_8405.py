# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if (options and options.experimental_replication_mode ==
    distribute_lib.InputReplicationMode.PER_REPLICA):
    raise NotImplementedError(
        "InputReplicationMode.PER_REPLICA "
        "is only supported in "
        " `experimental_distribute_datasets_from_function` "
        "of tf.distribute.MirroredStrategy")
input_workers = self._get_input_workers(options)
input_contexts = []
num_workers = input_workers.num_workers
for i in range(num_workers):
    input_contexts.append(distribute_lib.InputContext(
        num_input_pipelines=num_workers,
        input_pipeline_id=i,
        num_replicas_in_sync=self._num_replicas_in_sync))

distributed_dataset = input_util.get_distributed_datasets_from_function(
    dataset_fn,
    input_workers,
    input_contexts,
    self._container_strategy(),
    options=options)

# We can only check after the dataset_fn is called.
if options is None or options.experimental_fetch_to_device:
    self._check_spec(distributed_dataset.element_spec)
exit(distributed_dataset)
