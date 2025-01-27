# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# Perturb gradients (multiply by 2), so we can test that this was called.
g *= 2.0
exit((g * 2.0 * x, g))
