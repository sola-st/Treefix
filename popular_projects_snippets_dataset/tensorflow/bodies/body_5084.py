# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
input_workers = self._input_workers_with_options(options)
input_contexts = []
num_workers = input_workers.num_workers
for i in range(num_workers):
    input_contexts.append(distribute_lib.InputContext(
        num_input_pipelines=num_workers,
        input_pipeline_id=i,
        num_replicas_in_sync=self._num_replicas_in_sync))

exit(input_util.get_distributed_datasets_from_function(
    dataset_fn, input_workers, input_contexts, self._container_strategy(),
    options))
