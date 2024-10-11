# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
x = constant_op.constant([-1, 0., 1.])
with backprop.GradientTape() as tape:
    tape.watch(x)
    g = tape.gradient(math_ops.pow(x, 2), x)
g = self.evaluate(g)
self.assertAllClose([-2., 0., 2.], g)
