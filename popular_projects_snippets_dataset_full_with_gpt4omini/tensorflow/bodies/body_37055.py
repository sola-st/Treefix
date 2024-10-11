# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
asn1 = state_ops.assign_add(
    var_a, constant_op.constant(1), name="a_add")
asn2 = state_ops.assign_add(
    var_b, constant_op.constant(1), name="b_add")
with ops.control_dependencies([asn1, asn2]):
    inc_b = array_ops.identity(var_b)
exit(inc_b)
