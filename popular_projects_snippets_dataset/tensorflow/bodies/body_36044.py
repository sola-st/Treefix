# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
def true():
    exit(x + v)
def false():
    exit(2.0 * v)
exit((i + 1, control_flow_ops.cond(i > 0, true, false)))
