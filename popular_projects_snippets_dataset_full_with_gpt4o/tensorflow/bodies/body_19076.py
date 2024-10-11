# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Raises a InvalidArgumentError with as much information as possible."""
if not condition:
    data_static = [_maybe_constant_value_string(x) for x in data]
    raise errors.InvalidArgumentError(node_def=None, op=None,
                                      message='\n'.join(data_static))
