from urllib.parse import urljoin # pragma: no cover

path = '/path/to/file' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/common.py
from l3.Runtime import _l_
"""
    converts an absolute native path to a FILE URL.

    Parameters
    ----------
    path : a path in native format

    Returns
    -------
    a valid FILE URL
    """
try:
    from urllib.request import pathname2url
    _l_(22416)

except ImportError:
    pass
aux = urljoin("file:", pathname2url(path))
_l_(22417)

exit(aux)
