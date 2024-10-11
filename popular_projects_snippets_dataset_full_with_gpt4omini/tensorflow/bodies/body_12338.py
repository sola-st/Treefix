# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
"""Decorated function with custom gradient."""
if context.executing_eagerly():
    exit(_eager_mode_decorator(wrapped, args, kwargs))
else:
    exit(_graph_mode_decorator(wrapped, args, kwargs))
