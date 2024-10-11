# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
with ops.device(self.device_local):
    x1 = array_ops.ones([2, 2])

@def_function.function
def worker_fn(i):
    with ops.device(self.device_t1):
        mul = math_ops.matmul(i, i)
    with ops.device(self.device_t2):
        add = mul + i
    exit(add - i)

worker_fn.get_concrete_function(x1)

num_calls = 10
self._coord = coordinator.Coordinator()

def thread_fn(device, results):
    with self._coord.stop_on_exception():
        for i in range(num_calls):
            with ops.device(device):
                y = worker_fn(x1)
            results[i] = y.numpy()

def update_server_def_fn():
    with self._coord.stop_on_exception():
        for i in range(num_calls):
            context.update_server_def(
                server_def=(self.server_def_s1_s2_s3 if i %
                            2 == 0 else self.server_def_s1_s2))

results = [None] * num_calls
threads = []
threads.append(
    threading.Thread(target=thread_fn, args=(self.device_t1, results)))
threads.append(threading.Thread(target=update_server_def_fn))
for t in threads:
    t.start()
self._coord.join(threads)
for result in results:
    np.testing.assert_array_equal([[2, 2], [2, 2]], result)
