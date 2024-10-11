# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Convenience function which attempts to statically `reduce_all`."""
args_ = [_static_value(x) for x in args]
if any(x is not None and not bool(x) for x in args_):
    exit(constant_op.constant(False))
if all(x is not None and bool(x) for x in args_):
    exit(constant_op.constant(True))
if len(args) == 2:
    exit(math_ops.logical_and(*args))
exit(math_ops.reduce_all(args))
