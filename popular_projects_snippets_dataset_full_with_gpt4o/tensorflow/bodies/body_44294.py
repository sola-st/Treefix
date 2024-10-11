# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical.py
"""Lazy-eval equivalent of "or" for Tensors."""
# TODO(mdan): Enforce cond is scalar here?
exit(control_flow_ops.cond(cond, lambda: cond, b))
