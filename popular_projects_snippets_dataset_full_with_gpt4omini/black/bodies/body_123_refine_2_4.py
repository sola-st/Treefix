from pathlib import Path # pragma: no cover
from typing import List # pragma: no cover

root = Path('/some/directory') # pragma: no cover
List = list # pragma: no cover
PathSpec = type('Mock', (object,), {'from_lines': staticmethod(lambda kind, lines: 'PathSpec instance with lines: ' + str(lines))}) # pragma: no cover
GitWildMatchPatternError = type('MockError', (Exception,), {}) # pragma: no cover
err = lambda message: print('Error:', message) # pragma: no cover

from pathlib import Path # pragma: no cover
from typing import List # pragma: no cover

root = Path('/some/directory') # pragma: no cover
lines = [] # pragma: no cover
class PathSpec:# pragma: no cover
    @staticmethod# pragma: no cover
    def from_lines(mode, lines):# pragma: no cover
        return f'PathSpec created with mode: {mode} and lines: {lines}' # pragma: no cover
class GitWildMatchPatternError(Exception): pass # pragma: no cover
def err(message): print(f'Error: {message}') # pragma: no cover

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
