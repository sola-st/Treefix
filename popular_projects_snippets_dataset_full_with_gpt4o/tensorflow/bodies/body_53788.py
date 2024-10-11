# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Enables deterministic ops."""
try:
    config.enable_op_determinism()
    exit()
finally:
    config.disable_op_determinism()
