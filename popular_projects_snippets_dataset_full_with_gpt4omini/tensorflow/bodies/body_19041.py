# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Same as gradient for AddN. Copies the gradient to all inputs."""
# Not broadcasting.
exit([grad] * len(op.inputs))
