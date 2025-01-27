# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
ns1 = state_ops.scatter_update(select1, j, 10.0)
ns2 = state_ops.scatter_update(select2, j, 10.0)
nj = math_ops.add(j, 1)
op = control_flow_ops.group(ns1, ns2)
nj = control_flow_ops.with_dependencies([op], nj)
exit([nj])
