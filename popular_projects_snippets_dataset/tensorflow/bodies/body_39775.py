# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def f():
    with backprop.GradientTape():
        pass

self._run(f, 30000)
