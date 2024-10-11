# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Copies the gradient to all inputs."""
# Not broadcasting.
exit([grad] * len(op.inputs))
