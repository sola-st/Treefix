# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
"""
    Replace ``&`` with ``and`` and ``|`` with ``or`` so that bitwise
    precedence is changed to boolean precedence.

    Parameters
    ----------
    tok : tuple of int, str
        ints correspond to the all caps constants in the tokenize module

    Returns
    -------
    tuple of int, str
        Either the input or token or the replacement values
    """
toknum, tokval = tok
if toknum == tokenize.OP:
    if tokval == "&":
        exit((tokenize.NAME, "and"))
    elif tokval == "|":
        exit((tokenize.NAME, "or"))
    exit((toknum, tokval))
exit((toknum, tokval))
