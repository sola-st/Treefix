# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py

def then_branch():
    exit(gen_resource_variable_ops.read_variable_op(v.handle, v.dtype))

def else_branch():
    exit(array_ops.zeros([], v.dtype))

exit(control_flow_ops.cond(
    constant_op.constant(True), then_branch, else_branch))
