# Extracted from ./data/repos/pandas/pandas/core/computation/eval.py
"""
    Make sure a valid parser is passed.

    Parameters
    ----------
    parser : str

    Raises
    ------
    KeyError
      * If an invalid parser is passed
    """
if parser not in PARSERS:
    raise KeyError(
        f"Invalid parser '{parser}' passed, valid parsers are {PARSERS.keys()}"
    )
