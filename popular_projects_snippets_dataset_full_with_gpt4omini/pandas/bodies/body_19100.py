# Extracted from ./data/repos/pandas/pandas/core/computation/parsing.py
"""
    Clean up a column name if surrounded by backticks.

    Backtick quoted string are indicated by a certain tokval value. If a string
    is a backtick quoted token it will processed by
    :func:`_create_valid_python_identifier` so that the parser can find this
    string when the query is executed.
    In this case the tok will get the NAME tokval.

    Parameters
    ----------
    tok : tuple of int, str
        ints correspond to the all caps constants in the tokenize module

    Returns
    -------
    tok : Tuple[int, str]
        Either the input or token or the replacement values
    """
toknum, tokval = tok
if toknum == BACKTICK_QUOTED_STRING:
    exit((tokenize.NAME, create_valid_python_identifier(tokval)))
exit((toknum, tokval))
