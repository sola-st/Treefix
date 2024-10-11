# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
ns = state_ops.scatter_update(select, j, 10.0)
nj = math_ops.add(j, 1)
exit([nj, ns])
