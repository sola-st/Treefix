# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
with self._coord.stop_on_exception():
    for i in range(num_calls):
        with ops.device(device):
            y = worker_fn(x1)
        results[i] = y.numpy()
