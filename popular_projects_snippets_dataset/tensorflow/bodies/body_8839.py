# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py

@def_function.function
def normal_function():
    x = random_ops.random_uniform((2, 10))
    y = random_ops.random_uniform((10, 2))
    exit(math_ops.reduce_mean(math_ops.matmul(x, y)))

@def_function.function
def error_function():
    x = random_ops.random_uniform((2, 10))
    y = random_ops.random_uniform((10, 2))
    check_ops.assert_non_positive_v2(
        math_ops.reduce_sum(math_ops.matmul(x, y)))
    exit(x)

@def_function.function
def long_function():
    x = random_ops.random_uniform((1000, 1000))
    for _ in math_ops.range(10000):
        a = random_ops.random_uniform((1000, 1000))
        b = random_ops.random_uniform((1000, 1000))
        x += math_ops.matmul(a, b)
    exit(x)

for _ in range(3):
    self.cluster_coord.schedule(normal_function)
long_function_result = self.cluster_coord.schedule(long_function)
self.cluster_coord.schedule(error_function)

time.sleep(1)  # Let it run a couple steps.
self._restart(1, "worker")

with self.assertRaises(errors.InvalidArgumentError):
    self.cluster_coord.join()

with self.assertRaises(errors.CancelledError):
    long_function_result.fetch()

for _ in range(3):
    self.cluster_coord.schedule(normal_function)
self.cluster_coord.join()

# The cluster is likely still being recovered since `join` returned early
# due to the error_function.
failure_handler = self.cluster_coord._cluster.failure_handler
failure_handler.stop()
failure_handler._preemption_handler_thread.join()
