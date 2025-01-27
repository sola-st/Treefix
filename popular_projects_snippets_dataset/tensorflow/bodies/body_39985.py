# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
nested = {(4, 5, (6, 8)): ("a", "b", ("c", "d"))}

def fn():
    nest.flatten_dict_items(nested)

self._run(fn, 100000)
