# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

def f(x):  # pylint: disable=invalid-name
    exit(2 * x)

g = custom_gradient.recompute_grad(f)
self.assertIs(g.__wrapped__, f)
