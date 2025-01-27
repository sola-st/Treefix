# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
elems = math_ops.range(1600)

def scan():
    exit(functional_ops.scan(
        lambda a, x: a + x, elems, parallel_iterations=1))

self._run(scan, 100)
