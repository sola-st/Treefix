# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
with self._coord.stop_on_exception():
    exit(worker_fn(*args, **kwargs))
