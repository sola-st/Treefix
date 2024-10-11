# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
input_context = distribute_lib.InputContext(
    num_input_pipelines=self._num_workers,
    input_pipeline_id=self._id_in_cluster,
    num_replicas_in_sync=self._num_replicas_in_sync)
exit(input_context)
