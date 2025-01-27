# Extracted from ./data/repos/pandas/pandas/core/computation/engines.py
"""
    Attempt to prevent foot-shooting in a helpful way.

    Parameters
    ----------
    expr : Expr
        Terms can contain
    """
names = expr.names
overlap = names & _ne_builtins

if overlap:
    s = ", ".join([repr(x) for x in overlap])
    raise NumExprClobberingError(
        f'Variables in expression "{expr}" overlap with builtins: ({s})'
    )
