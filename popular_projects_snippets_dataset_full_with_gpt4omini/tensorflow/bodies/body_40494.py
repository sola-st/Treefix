# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as g:
    x = constant_op.constant([[1., 2], [3, 4]])
    g.watch(x)
    y = math_ops.matmul(x, x)
self.assertAllClose(
    g.jacobian(y, x, parallel_iterations=2),
    g.jacobian(y, x, parallel_iterations=3))
