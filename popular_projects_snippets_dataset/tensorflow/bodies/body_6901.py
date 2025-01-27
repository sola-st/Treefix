# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
assert isinstance(input_workers, InputWorkers)
if not input_workers.worker_devices:
    raise ValueError("Should have at least one worker for input iterator.")

self._iterators = iterators
self._input_workers = input_workers
self._strategy = strategy
self._cardinality = cardinality
self._enable_get_next_as_optional = enable_get_next_as_optional
