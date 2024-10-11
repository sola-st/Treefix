# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
with self._coord.stop_on_exception():
    for i in range(num_calls):
        with context.executor_scope(executor_obj):
            with ops.device(device):
                results[i] = worker_fn()
