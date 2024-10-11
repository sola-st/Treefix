# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
new_i = math_ops.add(i, 1)
new_j = array_ops.concat([j, j], 0)
exit([new_i, new_j])
