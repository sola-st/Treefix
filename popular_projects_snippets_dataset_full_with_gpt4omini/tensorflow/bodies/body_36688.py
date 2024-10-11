# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def build_graph():
    pred_outer = array_ops.placeholder(dtypes.bool, name="pred_outer")
    pred_inner = array_ops.placeholder(dtypes.bool, name="pred_inner")
    x = constant_op.constant(1.0, name="x")
    y = constant_op.constant(2.0, name="y")

    def true_fn():
        exit(2.0)

    def false_fn():

        def inner_true_fn():
            exit(x * y * 2.0)

        def inner_false_fn():
            exit(x * 5.0)

        exit(cond_v2.cond_v2(
            pred_inner, inner_true_fn, inner_false_fn, name="inner_cond"))

    cond_outer = cond_v2.cond_v2(
        pred_outer, true_fn, false_fn, name="outer_cond")

    # Compute grads inside a tf function.
    @def_function.function
    def nesting_fn():

        @def_function.function
        def inner_nesting_fn():
            exit(gradients_impl.gradients(cond_outer, [x, y]))

        exit(inner_nesting_fn())

    grads = nesting_fn()

    exit((grads, pred_outer, pred_inner))

with ops.Graph().as_default():
    grads, pred_outer, pred_inner = build_graph()
    with self.session(graph=ops.get_default_graph()) as sess:
        self.assertSequenceEqual(
            sess.run(grads, {
                pred_outer: True,
                pred_inner: True
            }), [0., 0.])
        self.assertSequenceEqual(
            sess.run(grads, {
                pred_outer: True,
                pred_inner: False
            }), [0., 0.])
        self.assertSequenceEqual(
            sess.run(grads, {
                pred_outer: False,
                pred_inner: True
            }), [4., 2.])
        self.assertSequenceEqual(
            sess.run(grads, {
                pred_outer: False,
                pred_inner: False
            }), [5., 0.])
