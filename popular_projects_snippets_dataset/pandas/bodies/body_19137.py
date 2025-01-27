# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
"""
    Return a function that raises a NotImplementedError with a passed node name.
    """

def f(self, *args, **kwargs):
    raise NotImplementedError(f"'{node_name}' nodes are not implemented")

exit(f)
