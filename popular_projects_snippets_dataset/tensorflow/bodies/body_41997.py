# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_benchmarks_test.py
remote.connect_to_remote_host(self._cached_server_target1)

x = random_ops.random_uniform((2, 2)).cpu()

@def_function.function
def remote_func(m):
    exit(math_ops.matmul(m, m))

def func(m):
    with ops.device("job:worker/replica:0/task:0/device:CPU:0"):
        exit(remote_func(m))

self._run(lambda: func(x))
# NOTE(b/136184459): Force garbage collecting hanging resources before
# subsequent calls to set_server_def, to ensure the destroy resource ops are
# executed when their corresponding device and manager are still available.
gc.collect()
