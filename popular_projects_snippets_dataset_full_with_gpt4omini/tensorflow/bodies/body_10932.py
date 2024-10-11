# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# Perturb gradients (multiply by 3), so we can test that this was called.
grad *= 3.0
exit((grad * op.inputs[0] * 2.0, grad))
