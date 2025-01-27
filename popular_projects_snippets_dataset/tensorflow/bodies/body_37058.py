# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
asn1 = state_ops.assign_add(var_a, 1, name="a_add")
with ops.control_dependencies([asn1]):
    asn2 = state_ops.assign_add(var_b, var_a, name="b_add")
with ops.control_dependencies([asn2]):
    ni = math_ops.add(i, 1, name="i_add")
    exit(ni)
