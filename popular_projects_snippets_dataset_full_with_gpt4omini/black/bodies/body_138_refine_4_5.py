import sys # pragma: no cover
def parse_single_version(src, version): return True # pragma: no cover

src = '' # pragma: no cover
sys = type('Mock', (object,), {'version_info': (3, 9)})() # pragma: no cover

import sys # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

src = '3.9.0' # pragma: no cover
def parse_single_version(src, version):# pragma: no cover
    if src == '3.9.0' and version == (3, 9):# pragma: no cover
        return 0# pragma: no cover
    raise SyntaxError('Invalid version') # pragma: no cover
sys.version_info = (3, 9) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
# TODO: support Python 4+ ;)
from l3.Runtime import _l_
versions = [(3, minor) for minor in range(3, sys.version_info[1] + 1)]
_l_(5814)

first_error = ""
_l_(5815)
for version in sorted(versions, reverse=True):
    _l_(5821)

    try:
        _l_(5820)

        aux = parse_single_version(src, version)
        _l_(5816)
        exit(aux)
    except SyntaxError as e:
        _l_(5819)

        if not first_error:
            _l_(5818)

            first_error = str(e)
            _l_(5817)

raise SyntaxError(first_error)
_l_(5822)
