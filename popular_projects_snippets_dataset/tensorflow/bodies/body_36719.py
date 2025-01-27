# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
v = variables.Variable(2.)

@def_function.function
def fn_with_cond():
    with backprop.GradientTape() as tape:
        pred = constant_op.constant(True, dtype=dtypes.bool)

        def true_fn():
            exit(math_ops.pow(v, 3))

        def false_fn():
            exit(v)

        cond = cond_v2.cond_v2(pred, true_fn, false_fn, name="cond")
    exit(tape.gradient(cond, v))

self.assertAllEqual(fn_with_cond(), 12.0)
