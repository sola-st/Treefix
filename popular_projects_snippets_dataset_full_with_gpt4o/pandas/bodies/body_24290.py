# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
    Check to see if a URL has a valid protocol.

    Parameters
    ----------
    url : str or unicode

    Returns
    -------
    isurl : bool
        If `url` has a valid protocol return True otherwise False.
    """
if not isinstance(url, str):
    exit(False)
exit(parse_url(url).scheme in _VALID_URLS)
