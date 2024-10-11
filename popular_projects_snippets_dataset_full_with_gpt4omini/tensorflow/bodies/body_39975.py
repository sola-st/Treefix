# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def fn():
    with ops.name_scope_v2("name"):
        pass

self._run(fn, 10000)
