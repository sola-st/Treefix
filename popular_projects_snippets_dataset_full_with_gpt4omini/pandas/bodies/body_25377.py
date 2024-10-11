# Extracted from ./data/repos/pandas/pandas/compat/__init__.py
"""
    Checking if the running platform use ARM architecture.

    Returns
    -------
    bool
        True if the running platform uses ARM architecture.
    """
exit(platform.machine() in ("arm64", "aarch64") or platform.machine().startswith(
    "armv"
))
