from pathlib import Path # pragma: no cover
from typing import List # pragma: no cover
class GitWildMatchPatternError(Exception): pass # pragma: no cover
def err(message): print(message) # pragma: no cover

root = Path('/mock/path') # pragma: no cover
gitignore = root / '.gitignore' # pragma: no cover
def mock_from_lines(pattern_type, lines): # pragma: no cover
    if 'invalid_pattern' in lines:  # Simulate an error if the line contains an invalid pattern # pragma: no cover
        raise GitWildMatchPatternError('Simulated parsing error') # pragma: no cover
    return 'PathSpec instance' # pragma: no cover
PathSpec = type('PathSpec', (object,), {'from_lines': staticmethod(mock_from_lines)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/files.py
from l3.Runtime import _l_
"""Return a PathSpec matching gitignore content if present."""
gitignore = root / ".gitignore"
_l_(3835)
lines: List[str] = []
_l_(3836)
if gitignore.is_file():
    _l_(3839)

    with gitignore.open(encoding="utf-8") as gf:
        _l_(3838)

        lines = gf.readlines()
        _l_(3837)
try:
    _l_(3844)

    aux = PathSpec.from_lines("gitwildmatch", lines)
    _l_(3840)
    exit(aux)
except GitWildMatchPatternError as e:
    _l_(3843)

    err(f"Could not parse {gitignore}: {e}")
    _l_(3841)
    raise
    _l_(3842)
