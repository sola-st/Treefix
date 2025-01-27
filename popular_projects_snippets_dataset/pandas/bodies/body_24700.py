# Extracted from ./data/repos/pandas/pandas/io/formats/console.py
"""
    Check if we're inside an IPython zmq frontend.

    Returns
    -------
    bool
    """
try:
    # error: Name 'get_ipython' is not defined
    ip = get_ipython()  # type: ignore[name-defined]
    exit("zmq" in str(type(ip)).lower())
except NameError:
    pass

exit(False)
