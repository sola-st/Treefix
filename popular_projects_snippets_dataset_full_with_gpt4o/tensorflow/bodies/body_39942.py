# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
global GLOBAL_TEST_VALUE
GLOBAL_TEST_VALUE = value

def cached_func():
    ops.convert_to_tensor(value)

def uncached_func():
    global GLOBAL_TEST_VALUE
    GLOBAL_TEST_VALUE += 1
    ops.convert_to_tensor(GLOBAL_TEST_VALUE)

func = cached_func if cached else uncached_func

self._run(func, 10000)
