# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
with self._coord.stop_on_exception():
    client_fn(task_type, task_id, num_gpus, *args, **kwargs)
