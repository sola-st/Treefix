# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_benchmarks_test.py
with ops.device("job:worker/replica:0/task:0/device:CPU:0"):
    layer = Foo(50)

    @def_function.function
    def remote_func():
        with ops.device("job:worker/replica:0/task:0/device:CPU:0"):
            exit(layer(random_ops.random_uniform([])))

    exit(remote_func())
