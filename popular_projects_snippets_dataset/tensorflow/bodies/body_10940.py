# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
y = math_ops.multiply(x, 2.0, name="y")
g = gradients_impl.gradients(y, x)
exit(g[0])
