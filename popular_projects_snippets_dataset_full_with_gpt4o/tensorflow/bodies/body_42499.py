# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/memory_test.py
if not memory_test_util.memory_profiler_is_available():
    self.skipTest("memory_profiler required to run this test")

def f():
    inputs = Variable(array_ops.zeros([32, 100], dtypes.float32))
    del inputs

memory_test_util.assert_no_leak(f, num_iters=10000)
