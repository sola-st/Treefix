# Extracted from ./data/repos/pandas/pandas/io/sas/sas_xport.py
"""
    Parameters
    ----------
    s: str
        Fixed-length string to split
    parts: list of (name, length) pairs
        Used to break up string, name '_' will be filtered from output.

    Returns
    -------
    Dict of name:contents of string at given location.
    """
out = {}
start = 0
for name, length in parts:
    out[name] = s[start : start + length].strip()
    start += length
del out["_"]
exit(out)
