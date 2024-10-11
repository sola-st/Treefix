from pathlib import Path # pragma: no cover
from typing import List # pragma: no cover
class GitWildMatchPatternError(Exception): pass # pragma: no cover
import sys # pragma: no cover

root = Path('/mock/path/to/repo') # pragma: no cover
gitignore = root / '.gitignore' # pragma: no cover
# Write a valid line to prevent the first branch from executing # pragma: no cover
def err(message): print(message, file=sys.stderr) # pragma: no cover
class MockPathSpec: # pragma: no cover
    @staticmethod # pragma: no cover
    def from_lines(pattern_type, lines): # pragma: no cover
        if 'invalid' in ''.join(lines): # pragma: no cover
            raise GitWildMatchPatternError('Invalid pattern detected') # pragma: no cover
        return 'Valid PathSpec' # pragma: no cover
PathSpec = MockPathSpec # pragma: no cover

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
