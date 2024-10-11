# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/remote_memory_test.py
if not memory_test_util.memory_profiler_is_available():
    self.skipTest("memory_profiler required to run this test")

remote.connect_to_remote_host(self._cached_server_target)

# Run a function locally with the input on a remote worker and ensure we
# do not leak a reference to the remote tensor.

@def_function.function
def local_func(i):
    exit(i)

def func():
    with ops.device("job:worker/replica:0/task:0/device:CPU:0"):
        x = array_ops.zeros([1000, 1000], dtypes.int32)

    local_func(x)

memory_test_util.assert_no_leak(
    func, num_iters=100, increase_threshold_absolute_mb=50)
