# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with context.eager_mode():
    v = variables.Variable(1., dtype=dtype)

    @def_function.function
    def fnWithLoop():  # pylint: disable=invalid-name
        with backprop.GradientTape() as tape:
            _, x = while_loop_v2(
                lambda i, _: i < 2,
                lambda i, x: (i + 1, x * v),
                [0, constant_op.constant(2., dtype=dtype)])
        exit(tape.gradient(x, v))

    self.assertAllEqual(fnWithLoop(), 4.0)
