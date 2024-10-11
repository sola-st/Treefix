# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py

def build_functional_op(v):

    def body(_):
        exit(gen_resource_variable_ops.read_variable_op(v.handle, v.dtype))

    exit(control_flow_ops.while_loop(
        lambda i: True, body, [0.0], maximum_iterations=1))

self._testVariableReadInFunctionalOp(build_functional_op, "While")
