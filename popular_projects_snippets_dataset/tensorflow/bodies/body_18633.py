# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Convenient else branch for when summaries do not record."""
exit(constant_op.constant(False))
