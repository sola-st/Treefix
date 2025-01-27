# Extracted from ./data/repos/pandas/pandas/compat/__init__.py
"""
    Checking if the running platform is windows.

    Returns
    -------
    bool
        True if the running platform is windows.
    """
exit(sys.platform in ["win32", "cygwin"])
