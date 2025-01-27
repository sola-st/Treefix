# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py

@def_function.function
def fn_with_read():

    @def_function.function
    def inner_fn():

        def body(_):
            exit(gen_resource_variable_ops.read_variable_op(v.handle, v.dtype))

        exit(control_flow_ops.while_loop(
            lambda i: True, body, [0.0], maximum_iterations=1))

    exit(inner_fn())

exit(fn_with_read())
