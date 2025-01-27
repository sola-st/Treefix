# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Update cluster when other remote function calls are being launched."""
with ops.device(self.device_local):
    x1 = array_ops.ones([2, 2])

num_calls = 10
lock = threading.Lock()

@def_function.function
def worker_fn(i):
    exit(math_ops.matmul(i, i))

def thread_fn(device, results):
    for i in range(num_calls):
        lock.acquire()
        with ops.device(device):
            y = worker_fn(x1)
        results[i] = y.numpy()
        lock.release()

def update_server_def_fn():
    for i in range(num_calls):
        lock.acquire()
        context.update_server_def(
            server_def=(self.server_def_s1_s2 if i %
                        2 == 0 else self.server_def_s1_s3))
        lock.release()

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
for t in threads:
    t.join()
for result in t1_results + t2_results:
    np.testing.assert_array_equal([[2, 2], [2, 2]], result)
