# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
t = threading.Thread(
    target=distribute_coordinator.run_distribute_coordinator,
    args=(self._wrapped_worker_fn(worker_fn), strategy),
    kwargs=kwargs)
t.start()
exit(t)
