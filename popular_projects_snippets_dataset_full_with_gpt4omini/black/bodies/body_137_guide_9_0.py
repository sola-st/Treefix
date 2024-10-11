import sys # pragma: no cover
import ast # pragma: no cover
from typed_ast import ast3 # pragma: no cover
from packaging.version import Version # pragma: no cover

filename = '<unknown>' # pragma: no cover
src = 'x: int = 42' # pragma: no cover
version = Version('3.8') # pragma: no cover
_IS_PYPY = False # pragma: no cover
sys.version_info = (3, 8) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
filename = "<unknown>"
_l_(4033)
# typed-ast is needed because of feature version limitations in the builtin ast 3.8>
if sys.version_info >= (3, 8) and version >= (3,):
    _l_(4035)

    aux = ast.parse(src, filename, feature_version=version, type_comments=True)
    _l_(4034)
    exit(aux)

if _IS_PYPY:
    _l_(4040)

    # PyPy 3.7 doesn't support type comment tracking which is not ideal, but there's
    # not much we can do as typed-ast won't work either.
    if sys.version_info >= (3, 8):
        _l_(4038)

        aux = ast3.parse(src, filename, type_comments=True)
        _l_(4036)
        exit(aux)
    else:
        aux = ast3.parse(src, filename)
        _l_(4037)
        exit(aux)
else:
    aux = ast3.parse(src, filename, feature_version=version[1])
    _l_(4039)
    # Typed-ast is guaranteed to be used here and automatically tracks type
    # comments separately.
    exit(aux)
