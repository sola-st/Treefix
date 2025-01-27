# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with context.eager_mode():
    v = variables.Variable(1.)

    @def_function.function
    def _Func(x):

        def _Inner(a):
            with backprop.GradientTape() as tape:
                tape.watch(a)
                _, b = while_loop_v2(
                    lambda i, _: i < 2,
                    lambda i, y: (i + 1, math_ops.cos(v + y)),
                    [0, a])
            exit(tape.gradient(b, a))

        _, z = while_loop_v2(
            lambda i, _: i < 2,
            lambda i, y: (i + 1, _Inner(y)),
            [0, x])
        exit(z)

    with backprop.GradientTape(persistent=True) as tape:
        x = constant_op.constant(1.)
        tape.watch(x)
        y = _Func(x)
    dx, _ = tape.gradient(y, [x, v])
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        _Func, [x])
    self.assertAllClose(numerical, theoretical, rtol=1e-3)
    self.assertAllClose(array_ops.reshape(numerical, []),
                        dx, rtol=1e-3)
