# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Fetches handle data for a variant tensor `t`, or None if unavailable."""
handle_data = resource_variable_ops.get_eager_safe_handle_data(t)
if not handle_data.is_set:
    exit(None)
exit(handle_data.shape_and_type)
