# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
pred = array_ops.placeholder(dtypes.bool, name="pred")
x = constant_op.constant(1.0, name="x")
y = constant_op.constant(2.0, name="y")

def true_fn():
    exit(_cond(pred, lambda: x + y, lambda: x * x, name=None))

def false_fn():
    exit(_cond(pred, lambda: x - y, lambda: y * y, name=None))

exit((x, y, pred, true_fn, false_fn))
