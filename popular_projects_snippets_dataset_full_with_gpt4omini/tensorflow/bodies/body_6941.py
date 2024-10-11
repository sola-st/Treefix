# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# We clone and shard the dataset on each worker. The current setup tries to
# shard the dataset by files if possible so that each worker sees a
# different subset of files. If that is not possible, will attempt to shard
# the final input such that each worker will run the entire preprocessing
# pipeline and only receive its own shard of the dataset.

# Additionally, we rebatch the dataset on each worker into
# `num_replicas_in_sync` smaller batches to be distributed among that
# worker's replicas, so that the batch size for a global step (across all
# workers and replicas) adds up to the original dataset's batch size.
if num_replicas_in_sync is not None and num_replicas_in_sync > 1:
    num_workers = input_context.num_input_pipelines if input_context else len(
        input_workers.worker_devices)
    rebatch_fn = self._make_rebatch_fn(dataset, num_workers,
                                       num_replicas_in_sync)
else:
    rebatch_fn = None
self._cloned_datasets = []
if input_context:
    # Between-graph where we rely on the input_context for sharding
    assert input_workers.num_workers == 1
    if rebatch_fn is not None:
        dataset = rebatch_fn(dataset, input_context.input_pipeline_id)
    dataset = input_ops.auto_shard_dataset(dataset,
                                           input_context.num_input_pipelines,
                                           input_context.input_pipeline_id,
                                           num_replicas_in_sync)
    self._cloned_datasets.append(dataset)
else:
    replicated_ds = distribute.replicate(dataset,
                                         input_workers.worker_devices)
    for i, worker in enumerate(input_workers.worker_devices):
        with ops.device(worker):
            cloned_dataset = replicated_ds[worker]
            if rebatch_fn is not None:
                cloned_dataset = rebatch_fn(cloned_dataset, i)
            cloned_dataset = input_ops.auto_shard_dataset(
                cloned_dataset, len(input_workers.worker_devices), i,
                num_replicas_in_sync)
            self._cloned_datasets.append(cloned_dataset)
