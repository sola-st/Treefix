# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def func(x):
    exit(x)

self._run(lambda: (def_function.function(func)(x) for x in range(1000)),
          30000)
