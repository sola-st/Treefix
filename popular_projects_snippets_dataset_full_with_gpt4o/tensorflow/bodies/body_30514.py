# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
v = array_ops.broadcast_to(x, [2, 4, 3])
exit(2 * v)
