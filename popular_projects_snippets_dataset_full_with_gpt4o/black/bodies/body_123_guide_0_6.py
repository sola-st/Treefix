from pathspec import PathSpec # pragma: no cover
from pathlib import Path # pragma: no cover
import sys # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        pass # pragma: no cover
    @staticmethod # pragma: no cover
    def from_lines(*args): # pragma: no cover
        return 'PathSpec instance' # pragma: no cover
    is_file = lambda self: True # pragma: no cover
    open = lambda self, encoding='utf-8': MockFile() # pragma: no cover
class MockFile: # pragma: no cover
    def __enter__(self): # pragma: no cover
        return self # pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
        pass # pragma: no cover
    def readlines(self): # pragma: no cover
        return wildcard_patterns # pragma: no cover
wildcard_patterns = ['*.py'] # modify this for various test cases # pragma: no cover
PathSpec = Mock # pragma: no cover
GitWildMatchPatternError = Mock # pragma: no cover
err = print # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/files.py
from l3.Runtime import _l_
"""Return a PathSpec matching gitignore content if present."""
gitignore = root / ".gitignore"
_l_(15663)
lines: List[str] = []
_l_(15664)
if gitignore.is_file():
    _l_(15667)

    with gitignore.open(encoding="utf-8") as gf:
        _l_(15666)

        lines = gf.readlines()
        _l_(15665)
try:
    _l_(15672)

    aux = PathSpec.from_lines("gitwildmatch", lines)
    _l_(15668)
    exit(aux)
except GitWildMatchPatternError as e:
    _l_(15671)

    err(f"Could not parse {gitignore}: {e}")
    _l_(15669)
    raise
    _l_(15670)
