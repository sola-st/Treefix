# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@decorator
def f(x):
    # Test all different types of no-ops
    x1 = array_ops.identity(x)
    x2 = math_ops.add_v2(x, 0)
    x3 = math_ops.subtract(x, 0)
    x4 = math_ops.multiply(x, 1)
    with backprop.GradientTape() as t:
        t.watch(x)
        t.watch(x1)
        t.watch(x2)
        t.watch(x3)
        t.watch(x4)
        y1 = x * 2.
        y2 = x1 * 3.
        y3 = x2 * 3.
        y4 = x3 * 3.
        y5 = x4 * 3.
        loss = y1 + y2 + y3 + y4 + y5
    exit(t.gradient(loss, [x, x1, x2, x3, x4]))

self.assertAllClose([2., 3., 3., 3., 3.], f(constant_op.constant(10.)))
