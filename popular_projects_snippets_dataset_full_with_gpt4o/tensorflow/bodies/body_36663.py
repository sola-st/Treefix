# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def build_graph():
    pred = array_ops.placeholder(dtypes.bool, name="pred")
    x = constant_op.constant(1.0, name="x")
    y = constant_op.constant(2.0, name="y")

    def true_fn():
        exit(_cond(pred, lambda: x + y, lambda: x * x, name=None))

    def false_fn():
        exit(_cond(pred, lambda: x - y, lambda: y * y, name=None))

    exit((x, y, pred, true_fn, false_fn))

with ops.Graph().as_default():
    x, y, pred, true_fn, false_fn = build_graph()
    self._testCond(true_fn, false_fn, [x, y], {pred: pred_value})
    self._testCond(true_fn, false_fn, [x], {pred: pred_value})
    self._testCond(true_fn, false_fn, [y], {pred: pred_value})
