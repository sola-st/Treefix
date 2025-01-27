# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
y = math_ops.multiply(var, 2.0, name="y")
g = gradients_impl.gradients(y, var)
exit(g[0])
