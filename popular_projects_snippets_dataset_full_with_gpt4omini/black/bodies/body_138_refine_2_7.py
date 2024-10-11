import sys # pragma: no cover
from typing import Any # pragma: no cover

src = 'dummy_version_string' # pragma: no cover
def parse_single_version(src: str, version: tuple) -> Any: return 0 # pragma: no cover
sys.version_info = type('Mock', (object,), {'major': 3, 'minor': 9})() # pragma: no cover

import sys # pragma: no cover
from typing import Any # pragma: no cover

src = 'dummy_version_string' # pragma: no cover
def parse_single_version(src: str, version: tuple) -> Any: return 0 # pragma: no cover
sys.version_info = type('MockVersionInfo', (object,), {'major': 3, 'minor': 9, '__getitem__': lambda self, key: (self.major if key == 0 else self.minor)})() # pragma: no cover

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
