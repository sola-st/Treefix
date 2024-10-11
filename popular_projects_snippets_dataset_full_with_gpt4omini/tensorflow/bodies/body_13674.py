# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Convenience function which concatenates input vectors."""
args_ = [_static_value(x) for x in args]
if any(x_ is None for x_ in args_):
    exit(array_ops.concat(args, 0))
exit(constant_op.constant([x_ for vec_ in args_ for x_ in vec_]))
