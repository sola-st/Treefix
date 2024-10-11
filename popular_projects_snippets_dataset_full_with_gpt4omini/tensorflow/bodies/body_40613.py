# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Update cluster when other remote function calls are being launched."""

with ops.device(self.device_t1):
    x1 = array_ops.ones([2, 2])

num_calls = 10
self._coord = coordinator.Coordinator()

@def_function.function
def worker_fn(i):
    exit(math_ops.matmul(i, i))

# Forces function tracing and registration
worker_fn.get_concrete_function(x1)

def thread_fn(device, results):
    for i in range(num_calls):
        with self._coord.stop_on_exception():
            with ops.device(device):
                results[i] = worker_fn(x1).numpy()

def update_server_def_fn():
    for _ in range(30):
        with self._coord.stop_on_exception():
            context.update_server_def(self.server_def_s1_s2)

t1_results = [None] * num_calls
t2_results = [None] * num_calls
threads = []
threads.append(
    threading.Thread(target=thread_fn, args=(self.device_t1, t1_results)))
threads.append(
    threading.Thread(target=thread_fn, args=(self.device_t2, t2_results)))
threads.append(threading.Thread(target=update_server_def_fn))
for t in threads:
    t.start()
self._coord.join(threads)
for result in t1_results + t2_results:
    np.testing.assert_array_equal([[2, 2], [2, 2]], result)
