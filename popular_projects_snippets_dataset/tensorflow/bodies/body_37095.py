# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit(x + math_ops.reduce_sum(var.sparse_read([1, 3])))
