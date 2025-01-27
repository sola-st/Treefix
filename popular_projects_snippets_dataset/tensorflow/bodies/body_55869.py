# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py

def branch0():
    exit(array_ops.zeros([], v.dtype))

def branch1():
    gen_resource_variable_ops.assign_variable_op(v.handle, v + 1)
    exit(gen_resource_variable_ops.read_variable_op(v.handle, v.dtype))

exit(control_flow_ops.switch_case(
    constant_op.constant(0), [branch0, branch1]))
