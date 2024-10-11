# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
nested = {"a": [1, 2, 3], "b": (4, 5, 6)}
flat = nest.flatten(nested)

def fn():
    nest.pack_sequence_as(nested, flat)

self._run(fn, 10000)
