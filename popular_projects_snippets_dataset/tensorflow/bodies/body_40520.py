# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as g:
    x = constant_op.constant([[1., 2], [3, 4]])
    g.watch(x)
    w = constant_op.constant([[1., 2, 3, 4], [5, 6, 7, 8]])
    y = math_ops.matmul(x, w)
self.assertAllClose(
    g.batch_jacobian(y, x, parallel_iterations=2),
    g.batch_jacobian(y, x, parallel_iterations=3))
