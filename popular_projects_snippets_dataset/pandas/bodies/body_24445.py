# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
"""
    Check whether skipfooter is compatible with other kwargs in TextFileReader.

    Parameters
    ----------
    kwds : dict
        Keyword arguments passed to TextFileReader.

    Raises
    ------
    ValueError
        If skipfooter is not compatible with other parameters.
    """
if kwds.get("skipfooter"):
    if kwds.get("iterator") or kwds.get("chunksize"):
        raise ValueError("'skipfooter' not supported for iteration")
    if kwds.get("nrows"):
        raise ValueError("'skipfooter' not supported with 'nrows'")
