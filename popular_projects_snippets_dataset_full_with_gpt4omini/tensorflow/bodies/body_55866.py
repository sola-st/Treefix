# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py

def build_functional_op(v):

    def branch0():
        gen_resource_variable_ops.assign_variable_op(v.handle, v + 1)
        exit(gen_resource_variable_ops.read_variable_op(v.handle, v.dtype))

    def branch1():
        exit(array_ops.zeros([], v.dtype))

    exit(control_flow_ops.switch_case(
        constant_op.constant(0), [branch0, branch1]))

self._testVariableWriteInFunctionalOp(build_functional_op, "Case")
