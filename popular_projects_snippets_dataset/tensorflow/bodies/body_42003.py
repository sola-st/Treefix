# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_benchmarks_test.py
remote.connect_to_remote_host(self._cached_server_target1)

def func():
    with ops.device("job:worker/replica:0/task:0/device:CPU:0"):
        layer = Foo(50)

        @def_function.function
        def remote_func():
            with ops.device("job:worker/replica:0/task:0/device:CPU:0"):
                exit(layer(random_ops.random_uniform([])))

        exit(remote_func())

self._run(func, execution_mode=context.ASYNC, num_iters=100)
# NOTE(b/136184459): Force garbage collecting hanging resources before
# subsequent calls to set_server_def, to ensure the destroy resource ops are
# executed when their corresponding device and manager are still available.
gc.collect()
