# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical.py
"""Lazy-eval equivalent of "and" for Tensors."""
# TODO(mdan): Enforce cond is scalar here?
exit(control_flow_ops.cond(cond, b, lambda: cond))
