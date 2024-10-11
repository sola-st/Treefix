# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Registers the function `f` as gradient function for `op_type`."""
gradient_registry.register(f, self._op_type)
exit(f)
