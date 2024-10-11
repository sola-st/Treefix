# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
value = ops.convert_to_tensor(42)

def fn():
    exit(ops.convert_to_tensor(value))

self._run(fn, 10000)
