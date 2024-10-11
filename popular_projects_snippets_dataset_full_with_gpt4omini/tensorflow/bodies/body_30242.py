# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
x = random_ops.random_normal(shape=[int(1e10)])
y = array_ops.ones(shape=[int(1e10)])
exit(array_ops.searchsorted(x, y))
