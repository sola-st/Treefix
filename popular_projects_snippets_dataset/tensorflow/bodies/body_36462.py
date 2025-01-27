# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with context.eager_mode():
    c = constant_op.constant(10)

    @def_function.function
    def F():

        def Body(_):
            exit(ops.get_default_graph().capture_call_time_value(
                lambda: c, tensor_spec.TensorSpec([], dtypes.int32)))

        x, = while_loop_v2(lambda i: True, Body, [0], maximum_iterations=1)
        exit(x)

    self.assertAllEqual(F(), 10)
