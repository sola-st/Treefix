import sys # pragma: no cover
import ast # pragma: no cover
from types import SimpleNamespace # pragma: no cover

version = (3, 9) # pragma: no cover
src = 'sample source code' # pragma: no cover
_IS_PYPY = False # pragma: no cover
ast3 = type('Mock', (object,), {'parse': lambda self, src, filename, feature_version=None, type_comments=False: None})() # pragma: no cover
sys.version_info = SimpleNamespace(major=3, minor=9, micro=0, releaselevel='final', serial=0) # pragma: no cover

import sys # pragma: no cover
import ast # pragma: no cover

version = (3, 9) # pragma: no cover
src = 'sample source code' # pragma: no cover
_IS_PYPY = False # pragma: no cover
ast3 = type('MockAst3', (object,), {'parse': lambda src, filename, feature_version=None, type_comments=False: None}) # pragma: no cover
sys.version_info = (3, 9, 0) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
filename = "<unknown>"
_l_(15543)
# typed-ast is needed because of feature version limitations in the builtin ast 3.8>
if sys.version_info >= (3, 8) and version >= (3,):
    _l_(15545)

    aux = ast.parse(src, filename, feature_version=version, type_comments=True)
    _l_(15544)
    exit(aux)

if _IS_PYPY:
    _l_(15550)

    # PyPy 3.7 doesn't support type comment tracking which is not ideal, but there's
    # not much we can do as typed-ast won't work either.
    if sys.version_info >= (3, 8):
        _l_(15548)

        aux = ast3.parse(src, filename, type_comments=True)
        _l_(15546)
        exit(aux)
    else:
        aux = ast3.parse(src, filename)
        _l_(15547)
        exit(aux)
else:
    aux = ast3.parse(src, filename, feature_version=version[1])
    _l_(15549)
    # Typed-ast is guaranteed to be used here and automatically tracks type
    # comments separately.
    exit(aux)
