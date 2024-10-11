# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
def wrapped(*args, **kwargs):
    with self._coord.stop_on_exception():
        exit(worker_fn(*args, **kwargs))
exit(wrapped)
