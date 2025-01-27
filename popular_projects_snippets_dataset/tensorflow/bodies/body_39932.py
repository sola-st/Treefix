# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
exit(functional_ops.scan(
    lambda a, x: a + x, elems, parallel_iterations=1))
