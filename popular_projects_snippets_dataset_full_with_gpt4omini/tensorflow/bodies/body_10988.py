# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
result = x1 * x2
grad = lambda dy: (dy * x1, dy * x2)
exit((result, grad))
