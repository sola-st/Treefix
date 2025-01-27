# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
y1 = var1.sparse_read([1, 3])
y2 = x2 * 2
y3 = x3 * math_ops.reduce_sum(var2.sparse_read([0]))
exit((i + 1, y1, y2, y3))
