# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def fn():
    nest.flatten(None)

self._run(fn, 100000)
