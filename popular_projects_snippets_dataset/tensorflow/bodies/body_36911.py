# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
y1 = var.sparse_read([1, 2])
y2 = array_ops.gather(x1, [2]) * x2
y3 = x2 * [1., 1., 1.]
exit((y1, y2, y3))
