# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
assert not self._built
distribute_start_time_ns = time.time_ns()
self._datasets, element_spec = (
    _create_datasets_from_function_with_input_context(
        self._input_contexts, self._input_workers, self._dataset_fn))
if context.executing_eagerly():
    # Records the time to initialize the distributed dataset.
    context.async_wait()
    distribute_duration_ms = (time.time_ns() -
                              distribute_start_time_ns) // 1_000_000
    _distributed_dataset_from_function_initialization_time_milliseconds.get_cell(
        self._strategy.__class__.__name__,
        str(self._input_workers.num_workers)).add(distribute_duration_ms)

self._element_spec = _create_distributed_tensor_spec(
    self._strategy, element_spec)
self._cardinality = _cardinality(self._datasets[0])
self._enable_get_next_as_optional = _enable_get_next_as_optional(
    self._strategy, self._datasets[0], self._cardinality)
self._built = True
