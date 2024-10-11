# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
i1 = math_ops.add(i, 1)
with ops.device("/cpu:0"):
    s1 = math_ops.add(i, s)
exit((i1, s1))
