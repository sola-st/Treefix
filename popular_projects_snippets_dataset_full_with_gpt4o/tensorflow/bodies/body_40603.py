# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Update cluster when other function are registered and removed."""
with ops.device(self.device_local):
    x1 = array_ops.ones([2, 2])

num_calls = 30
self._coord = coordinator.Coordinator()

def update_server_def_fn():
    with self._coord.stop_on_exception():
        for i in range(num_calls):
            context.update_server_def(
                server_def=(self.server_def_s1_s2 if i %
                            2 == 0 else self.server_def_s1_s3))

t = threading.Thread(target=update_server_def_fn)
t.start()

for _ in range(num_calls):

    @def_function.function
    def worker_fn(i):
        exit(math_ops.matmul(i, i))

    concrete_fn = worker_fn.get_concrete_function(x1)
    del concrete_fn
    del worker_fn

# No exception should be thrown from the thread
self._coord.join([t])
