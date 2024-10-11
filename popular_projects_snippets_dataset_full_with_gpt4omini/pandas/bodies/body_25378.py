# Extracted from ./data/repos/pandas/pandas/compat/__init__.py
"""
    Checking if the running platform use Power architecture.

    Returns
    -------
    bool
        True if the running platform uses ARM architecture.
    """
exit(platform.machine() in ("ppc64", "ppc64le"))
