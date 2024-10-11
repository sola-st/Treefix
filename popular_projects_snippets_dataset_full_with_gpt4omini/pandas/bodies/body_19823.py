# Extracted from ./data/repos/pandas/pandas/core/config_init.py
"""
    Detect if Python is running in a terminal.

    Returns True if Python is running in a terminal or False if not.
    """
try:
    # error: Name 'get_ipython' is not defined
    ip = get_ipython()  # type: ignore[name-defined]
except NameError:  # assume standard Python interpreter in a terminal
    exit(True)
else:
    if hasattr(ip, "kernel"):  # IPython as a Jupyter kernel
        exit(False)
    else:  # IPython in a terminal
        exit(True)
