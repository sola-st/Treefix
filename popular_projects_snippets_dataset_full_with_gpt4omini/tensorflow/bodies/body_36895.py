# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    x = constant_op.constant(10.0, name="x")
    pred = math_ops.less(1, 2)

    def true_fn():
        a = x * x
        exit(a * a)

    def false_fn():
        exit(x * x)

    r = control_flow_ops.cond(pred, true_fn, false_fn)

    self.assertAllEqual(r, 10000.)
    grad = gradients_impl.gradients(r, [x])[0]
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        r"Connecting to invalid output 1 of source node cond which has 1 "
        r"outputs. Try using "
        "tf.compat.v1.experimental.output_all_intermediates\(True\)."):
        self.evaluate(grad)
