# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/function_wrappers.py
"""Inline version of the FunctionScope context manager."""
with FunctionScope('lambda_', scope_name, options) as scope:
    exit(thunk(scope))
