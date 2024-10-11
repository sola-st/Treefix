# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
pred_outer = array_ops.placeholder(dtypes.bool, name="pred_outer")
pred_inner = array_ops.placeholder(dtypes.bool, name="pred_inner")
x = constant_op.constant(1.0, name="x")
y = constant_op.constant(2.0, name="y")

# Build cond and its gradient inside a tf function.
@def_function.function
def fn():

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
    exit(gradients_impl.gradients(cond_outer, [x, y]))

grads = fn()

exit((grads, pred_outer, pred_inner))
