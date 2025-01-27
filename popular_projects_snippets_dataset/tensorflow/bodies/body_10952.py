# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
x = constant_op.constant(10.0, name="x")
y = math_ops.multiply(x, c, name="y")
# Regression test for b/122564611.
z = math_ops.multiply(c, y, name="z")
g = gradients_impl.gradients(z, x)
exit(g[0])
