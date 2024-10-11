# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
for i in range(num_calls):
    with self._coord.stop_on_exception():
        with ops.device(device):
            results[i] = worker_fn(x1).numpy()
