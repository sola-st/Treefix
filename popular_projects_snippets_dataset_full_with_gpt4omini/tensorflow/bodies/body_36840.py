# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
assign = resource_variable_ops.assign_variable_op(rv.handle, False)
with ops.control_dependencies([assign]):
    exit(array_ops.identity(t))
