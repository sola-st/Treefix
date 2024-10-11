# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
z = math_ops.multiply(y, 3.0, name="z")
g = gradients_impl.gradients(z, y)
exit(g[0])
