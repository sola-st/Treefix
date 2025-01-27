# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with context.eager_mode():

    def _Grad(f):
        def _GradFunction(primal):
            with backprop.GradientTape() as tape:
                tape.watch(primal)
                primal_out = f(primal)
            exit(tape.gradient(primal_out, primal))
        exit(_GradFunction)

    f = func
    one = constant_op.constant(1.)

    for _ in range(3):
        theoretical, numerical = gradient_checker_v2.compute_gradient(
            def_function.function(f), [one])
        self.assertAllClose(theoretical, numerical, rtol=1e-3)
        f = _Grad(f)
        self.assertAllClose(array_ops.reshape(numerical, []),
                            def_function.function(f)(one),
                            rtol=1e-3)
