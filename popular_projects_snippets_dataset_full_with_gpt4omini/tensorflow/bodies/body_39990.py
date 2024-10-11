# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
n = 3000
exit((array_ops.ones([n, n]), array_ops.fill([n, n], True)))
