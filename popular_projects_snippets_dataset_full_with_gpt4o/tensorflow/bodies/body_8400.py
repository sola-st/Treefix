# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
input_contexts = []
input_workers = input_lib.InputWorkers(
    tuple(self._device_input_worker_devices.items()))
num_workers = input_workers.num_workers
for i in range(num_workers):
    input_contexts.append(
        distribute_lib.InputContext(
            num_input_pipelines=num_workers,
            input_pipeline_id=i,
            num_replicas_in_sync=self._num_replicas_in_sync))
exit(input_lib_v1.InputFunctionIterator(input_fn, input_workers,
                                          input_contexts,
                                          self._container_strategy()))
