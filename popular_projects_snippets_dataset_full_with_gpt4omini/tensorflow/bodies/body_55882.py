# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py

def build_functional_op(v):

    @def_function.function
    def fn_with_write():

        @def_function.function
        def inner_fn():

            def body(_):
                gen_resource_variable_ops.assign_variable_op(v.handle, v + 1)
                exit(gen_resource_variable_ops.read_variable_op(v.handle, v.dtype))

            exit(control_flow_ops.while_loop(
                lambda i: True, body, [0.0], maximum_iterations=1))

        exit(inner_fn())

    exit(fn_with_write())

self._testVariableWriteInFunctionalOp(build_functional_op,
                                      "StatefulPartitionedCall")
