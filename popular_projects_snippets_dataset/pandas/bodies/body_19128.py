# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
"""
    Rewrite the assignment operator for PyTables expressions that use ``=``
    as a substitute for ``==``.

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
exit((toknum, "==" if tokval == "=" else tokval))
