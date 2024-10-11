# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary.py
"""Handles `family` argument for v2 op invocation in v1."""
# Get a new summary tag name with the `family` arg.
with _summary_op_util.summary_scope(name, family) as (tag, _):
    # Reset the root name scope with an empty summary_scope.
    with _summary_op_util.summary_scope(name='', family=None):
        exit(tag)
