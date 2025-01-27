# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/memory_test.py
if not memory_test_util.memory_profiler_is_available():
    self.skipTest("memory_profiler required to run this test")

def f():

    @def_function.function
    def graph(x):
        exit(x * x + x)

    graph(constant_op.constant(42))

memory_test_util.assert_no_leak(
    f, num_iters=1000, increase_threshold_absolute_mb=30)
