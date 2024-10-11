import sys # pragma: no cover
from typing import Tuple # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

sys = type('MockSys', (), {'version_info': (3, 8, 0)})() # pragma: no cover
parse_single_version = MagicMock(side_effect=lambda src, version: (src, version)) # pragma: no cover
src = 'some_version_string' # pragma: no cover

import sys # pragma: no cover
from typing import Tuple # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

sys = type('MockSys', (), {'version_info': (3, 8, 10)})() # pragma: no cover
def mock_parse_single_version(src: str, version: Tuple[int, int]) -> None: raise SyntaxError('Invalid syntax') # pragma: no cover
parse_single_version = MagicMock(side_effect=mock_parse_single_version) # pragma: no cover
src = 'some_version_string' # pragma: no cover

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
