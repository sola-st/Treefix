# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
for i in range(num_calls):
    lock.acquire()
    with ops.device(device):
        y = worker_fn(x1)
    results[i] = y.numpy()
    lock.release()
