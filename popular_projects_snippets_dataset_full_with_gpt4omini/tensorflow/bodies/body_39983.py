# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
nested = {"a": [1, 2, 3], "b": (4, 5, 6)}

def fn():
    nest.flatten(nested)

self._run(fn, 100000)
