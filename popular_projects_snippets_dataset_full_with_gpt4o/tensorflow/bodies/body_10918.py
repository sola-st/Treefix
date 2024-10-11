# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with self.cached_session():
    x = constant_op.constant(3.0)
    y = math_ops.square(x)
    y1 = math_ops.square(y)
    y2 = math_ops.square(y1)
    g = gradients.gradients([y, y2], x)
    self.assertAllClose(17502.0, g[0])
    g = gradients.gradients(y + y2, x)
    self.assertAllClose(17502.0, g[0])
    z = array_ops.identity(y)
    z2 = array_ops.identity(y2)
    g = gradients.gradients([z, z2], x)
    self.assertAllClose(17502.0, g[0])
