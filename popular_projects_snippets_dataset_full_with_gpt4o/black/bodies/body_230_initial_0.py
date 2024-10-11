import re # pragma: no cover

s = '\tHello World\n\tThis is a test\nNo leading tab here' # pragma: no cover
FIRST_NON_WHITESPACE_RE = re.compile(r'^(\s*\t+\s*\S)') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/strings.py
from l3.Runtime import _l_
"""
    Splits string into lines and expands only leading tabs (following the normal
    Python rules)
    """
lines = []
_l_(16627)
for line in s.splitlines():
    _l_(16633)

    # Find the index of the first non-whitespace character after a string of
    # whitespace that includes at least one tab
    match = FIRST_NON_WHITESPACE_RE.match(line)
    _l_(16628)
    if match:
        _l_(16632)

        first_non_whitespace_idx = match.start(1)
        _l_(16629)

        lines.append(
            line[:first_non_whitespace_idx].expandtabs()
            + line[first_non_whitespace_idx:]
        )
        _l_(16630)
    else:
        lines.append(line)
        _l_(16631)
aux = lines
_l_(16634)
exit(aux)
