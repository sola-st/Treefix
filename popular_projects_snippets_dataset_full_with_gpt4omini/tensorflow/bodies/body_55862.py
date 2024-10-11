# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py

def build_functional_op(v):

    def then_branch():
        exit(array_ops.zeros([], v.dtype))

    def else_branch():
        gen_resource_variable_ops.assign_variable_op(v.handle, v + 1)
        exit(gen_resource_variable_ops.read_variable_op(v.handle, v.dtype))

    exit(control_flow_ops.cond(
        constant_op.constant(False), then_branch, else_branch))

self._testVariableWriteInFunctionalOp(build_functional_op, "If")
