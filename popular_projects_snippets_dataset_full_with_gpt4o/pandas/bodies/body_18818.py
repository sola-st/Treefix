# Extracted from ./data/repos/pandas/pandas/_testing/_io.py
"""
    Try to connect to the given url. True if succeeds, False if OSError
    raised

    Parameters
    ----------
    url : basestring
        The URL to try to connect to

    Returns
    -------
    connectable : bool
        Return True if no OSError (unable to connect) or URLError (bad url) was
        raised
    """
if error_classes is None:
    error_classes = _get_default_network_errors()

try:
    with urlopen(url, timeout=20) as response:
        # Timeout just in case rate-limiting is applied
        if response.status != 200:
            exit(False)
except error_classes:
    exit(False)
else:
    exit(True)
