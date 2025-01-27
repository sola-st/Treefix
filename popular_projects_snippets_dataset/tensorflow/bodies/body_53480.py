# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Saves the `op_type` as the `Operation` type."""
if not isinstance(op_type, str):
    raise TypeError("op_type must be a string.")
if "," in op_type:
    raise TypeError("op_type must not contain a comma.")
self._op_type = op_type
if not isinstance(statistic_type, str):
    raise TypeError("statistic_type must be a string.")
if "," in statistic_type:
    raise TypeError("statistic_type must not contain a comma.")
self._statistic_type = statistic_type
