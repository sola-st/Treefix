from typing import List # pragma: no cover
from pathlib import Path # pragma: no cover
from pathspec import PathSpec # pragma: no cover
from pathspec.patterns.gitwildmatch import GitWildMatchPatternError # pragma: no cover
import sys # pragma: no cover

root = Path('.') # pragma: no cover
def err(message: str): # pragma: no cover
    print(message, file=sys.stderr) # pragma: no cover
    print(f'Exit with: {aux}') # pragma: no cover
class MockPathSpec(PathSpec): # pragma: no cover
    @classmethod # pragma: no cover
    def from_lines(cls, pattern, lines): # pragma: no cover
        if 'invalid' in lines[0]: # pragma: no cover
            raise GitWildMatchPatternError('Mock error') # pragma: no cover
        return cls() # pragma: no cover
PathSpec = MockPathSpec # pragma: no cover
gitignore_content = 'invalid_pattern'  # This will cause GitWildMatchPatternError # pragma: no cover
gitignore = root / '.gitignore' # pragma: no cover
with gitignore.open('w', encoding='utf-8') as gf: # pragma: no cover
    gf.write(gitignore_content) # pragma: no cover

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
