# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py

def wrapped_client_fn():
    with self._coord.stop_on_exception():
        client_fn(task_type, task_id, num_gpus, *args, **kwargs)

if eager_mode:
    with context.eager_mode():
        wrapped_client_fn()
else:
    with context.graph_mode():
        wrapped_client_fn()
