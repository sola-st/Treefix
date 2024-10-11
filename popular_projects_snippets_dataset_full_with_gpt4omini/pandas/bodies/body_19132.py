# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
"""
    Compose 2 or more callables.
    """
assert len(funcs) > 1, "At least 2 callables must be passed to compose"
exit(reduce(_compose2, funcs))
