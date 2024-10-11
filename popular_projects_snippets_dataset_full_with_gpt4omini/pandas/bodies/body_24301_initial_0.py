from urllib.parse import urljoin # pragma: no cover
from urllib.request import pathname2url # pragma: no cover

path = '/home/user/document.txt' # pragma: no cover
urljoin = lambda *args: '/'.join(args) # pragma: no cover

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
    _l_(10825)

except ImportError:
    pass
aux = urljoin("file:", pathname2url(path))
_l_(10826)

exit(aux)
