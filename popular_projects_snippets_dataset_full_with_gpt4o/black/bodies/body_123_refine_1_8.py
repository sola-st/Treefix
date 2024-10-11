from pathlib import Path # pragma: no cover
from typing import List # pragma: no cover
class GitWildMatchPatternError(Exception): pass # pragma: no cover
def err(message: str): print(message) # pragma: no cover

root = Path('.') # pragma: no cover
PathSpec = type('Mock', (object,), {'from_lines': lambda matching, lines: 'mocked_pathspec'}) # pragma: no cover

from pathlib import Path # pragma: no cover
from typing import List # pragma: no cover
class GitWildMatchPatternError(Exception): pass # pragma: no cover
def err(message: str): print(message) # pragma: no cover

root = Path('.') # pragma: no cover
PathSpec = type('Mock', (object,), {'from_lines': lambda matching, lines: Path('/mocked_pathspec')}) # pragma: no cover

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
