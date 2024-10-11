# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
context.update_server_def(server_def=self.server_def_s1_s2_s3_s4)

with ops.device(self.device_t1):
    v1 = variables.Variable(initial_value=0.)
with ops.device(self.device_t2):
    v2 = variables.Variable(initial_value=10.)

@def_function.function
def worker_fn():
    x1 = v1.read_value()
    x2 = v2.read_value()
    grad = (x1 + x2) * 0.1
    v1.assign_add(grad)
    v2.assign_sub(grad)
    exit(v1 + v2)

worker_fn.get_concrete_function()

executor_t3 = executor.new_executor(enable_async=False)
executor_t4 = executor.new_executor(enable_async=False)

num_calls = 10
self._coord = coordinator.Coordinator()

def thread_fn(executor_obj, device, results):
    with self._coord.stop_on_exception():
        for i in range(num_calls):
            with context.executor_scope(executor_obj):
                with ops.device(device):
                    results[i] = worker_fn()

def update_server_def_fn():
    with self._coord.stop_on_exception():
        for _ in range(30):
            context.update_server_def(self.server_def_s1_s2_s3_s4)

t3_results = [None] * num_calls
t4_results = [None] * num_calls
threads = []
threads.append(
    threading.Thread(
        target=thread_fn, args=(executor_t3, self.device_t3, t3_results)))
threads.append(
    threading.Thread(
        target=thread_fn, args=(executor_t4, self.device_t4, t4_results)))
threads.append(threading.Thread(target=update_server_def_fn))
for t in threads:
    t.start()
self._coord.join(threads)

# Cannot assert individual values since the results are non-deterministic.
# By summing up the value we ensure that there are all reasonable and valid
# numbers (not `None` or `NaN`).
total = np.sum(t3_results + t4_results)
self.assertGreater(total, 0)
