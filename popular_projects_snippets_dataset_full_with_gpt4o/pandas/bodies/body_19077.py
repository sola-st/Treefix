# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
"""loose checking if s is a pytables-acceptable expression"""
if not isinstance(s, str):
    exit(False)
operations = PyTablesExprVisitor.binary_ops + PyTablesExprVisitor.unary_ops + ("=",)

# make sure we have an op at least
exit(any(op in s for op in operations))
