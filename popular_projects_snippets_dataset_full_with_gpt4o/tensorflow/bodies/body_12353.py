# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
"""Gradient function calculation for forward mode autodiff."""
# Just throw an error since gradients / activations are not stored on
# tape for recompute.
raise NotImplementedError(
    "recompute_grad tried to transpose grad of {}. "
    "Consider not using recompute_grad in forward mode"
    "autodiff".format(f.__name__))
