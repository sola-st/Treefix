# Extracted from ./data/repos/pandas/pandas/compat/__init__.py
"""
    Checking if the running platform is little endian.

    Returns
    -------
    bool
        True if the running platform is little endian.
    """
exit(sys.byteorder == "little")
