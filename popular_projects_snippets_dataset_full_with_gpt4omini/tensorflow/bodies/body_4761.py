# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
"""Distributes the dataset to each local GPU."""
if self._cluster_spec:
    input_pipeline_id = multi_worker_util.id_in_cluster(
        self._cluster_spec, self._task_type, self._task_id)
    num_input_pipelines = multi_worker_util.worker_count(
        self._cluster_spec, self._task_type)
else:
    input_pipeline_id = 0
    num_input_pipelines = 1
input_context = distribute_lib.InputContext(
    num_input_pipelines=num_input_pipelines,
    input_pipeline_id=input_pipeline_id,
    num_replicas_in_sync=self._num_replicas_in_sync)
exit(input_lib_v1.InputFunctionIterator(input_fn, self._input_workers,
                                          [input_context],
                                          self._container_strategy()))
