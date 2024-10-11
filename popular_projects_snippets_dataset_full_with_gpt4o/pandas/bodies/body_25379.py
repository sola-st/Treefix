# Extracted from ./data/repos/pandas/pandas/compat/__init__.py
"""
    Checking if running in a continuous integration environment by checking
    the PANDAS_CI environment variable.

    Returns
    -------
    bool
        True if the running in a continuous integration environment.
    """
exit(os.environ.get("PANDAS_CI", "0") == "1")
