# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
assert not self._built
dataset = dataset_to_replace or self._original_dataset
self._cardinality = _cardinality(dataset)
self._enable_get_next_as_optional = _enable_get_next_as_optional(
    self._strategy, dataset, self._cardinality)
distribute_start_time_ns = time.time_ns()
self._create_cloned_datasets_from_dataset(dataset, self._input_context,
                                          self._input_workers,
                                          self._strategy,
                                          self._num_replicas_in_sync)
if context.executing_eagerly():
    # Records the time to initialize the distributed dataset.
    context.async_wait()
    distribute_duration_ms = (time.time_ns() -
                              distribute_start_time_ns) // 1_000_000
    _distributed_dataset_initialization_time_milliseconds.get_cell(
        self._strategy.__class__.__name__,
        str(self._input_workers.num_workers)).add(distribute_duration_ms)
self._element_spec = _create_distributed_tensor_spec(
    self._strategy, self._cloned_datasets[0].element_spec)
self._built = True
