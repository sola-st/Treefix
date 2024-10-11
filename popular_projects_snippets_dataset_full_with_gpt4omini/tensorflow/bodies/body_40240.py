# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Computes the gradient of the decorated function."""

_, grad = val_and_grad_function(f, params=params)(*args, **kwds)
exit(grad)
