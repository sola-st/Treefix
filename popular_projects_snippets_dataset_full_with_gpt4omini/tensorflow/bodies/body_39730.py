# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
global GLOBAL_TEST_VALUE
GLOBAL_TEST_VALUE = value

def cached_func():
    constant_op.constant(value, dtype=dtype)

def uncached_func():
    global GLOBAL_TEST_VALUE
    GLOBAL_TEST_VALUE += 1
    constant_op.constant(GLOBAL_TEST_VALUE, dtype=dtype)

func = cached_func if cached else uncached_func

with ops.device("GPU:0" if context.num_gpus() else "CPU:0"):
    for _ in range(1000):
        func()  # Warmup.
    self._run(func, 3000)
