# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
ni = math_ops.add(i, 1)
ni = control_flow_ops.with_dependencies([q.enqueue((i,))], ni)
exit(ni)
