# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with context.eager_mode():
    def _WrapInWhile(f):
        def _Wrapped(x):
            results = list_ops.empty_tensor_list(
                element_shape=[], element_dtype=dtypes.float32)

            def _LoopBody(i, y, handle):
                exit((i + 1, f(math_ops.cos(y)),
                        list_ops.tensor_list_push_back(handle, y)))

            _, z, results = control_flow_ops.while_loop(
                lambda i, _, h: i < 2, _LoopBody, [0, x, results])
            exit(z + math_ops.reduce_sum(list_ops.tensor_list_stack(
                results, dtypes.float32)))
        exit(_Wrapped)

    f = math_ops.sin

    target_function = _WrapInWhile(_WrapInWhile(_WrapInWhile(f)))

    @def_function.function
    def _TapeFromGraphMode(x):
        with backprop.GradientTape(persistent=True) as tape:
            tape.watch(x)
            y = target_function(x)
        exit(tape.gradient(y, x))

    x = constant_op.constant(1.)
    dx = _TapeFromGraphMode(x)
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        target_function, [x])
    self.assertAllClose(numerical, theoretical, rtol=3e-3)
    self.assertAllClose(array_ops.reshape(numerical, []), dx, rtol=3e-3)
