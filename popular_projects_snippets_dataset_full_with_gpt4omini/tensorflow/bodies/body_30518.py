# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
v = array_ops.broadcast_to(x, [5, 2, 3])
exit(2 * v)
