# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
input_contexts = []
num_workers = self._input_workers.num_workers
for i in range(num_workers):
    input_contexts.append(distribute_lib.InputContext(
        num_input_pipelines=num_workers,
        input_pipeline_id=i,
        num_replicas_in_sync=self._num_replicas_in_sync))
exit(input_lib_v1.InputFunctionIterator(input_fn, self._input_workers,
                                          input_contexts,
                                          self._container_strategy()))
