# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def build_graph():
    pred = array_ops.placeholder(dtypes.bool, name="pred")
    x = constant_op.constant(1.0, name="x")
    y = constant_op.constant(2.0, name="y")

    def true_fn():
        exit(2.0)

    def false_fn():

        def false_true_fn():
            exit(x * y * 2.0)

        def false_false_fn():
            exit(x * 5.0)

        exit(_cond(pred, false_true_fn, false_false_fn, "inside_false_fn"))

    exit((x, y, pred, true_fn, false_fn))

with ops.Graph().as_default():
    x, y, pred, true_fn, false_fn = build_graph()
    self._testCond(true_fn, false_fn, [x, y], {pred: pred_value})
    self._testCond(true_fn, false_fn, [x], {pred: pred_value})
    self._testCond(true_fn, false_fn, [y], {pred: pred_value})
