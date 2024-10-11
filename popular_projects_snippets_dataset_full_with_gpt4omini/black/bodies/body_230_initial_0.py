import re # pragma: no cover

s = '\t   Example line 1\n\tExample line 2\nNo tabs here' # pragma: no cover
FIRST_NON_WHITESPACE_RE = re.compile('^(\s*\t)', re.MULTILINE) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/strings.py
from l3.Runtime import _l_
"""
    Splits string into lines and expands only leading tabs (following the normal
    Python rules)
    """
lines = []
_l_(4853)
for line in s.splitlines():
    _l_(4859)

    # Find the index of the first non-whitespace character after a string of
    # whitespace that includes at least one tab
    match = FIRST_NON_WHITESPACE_RE.match(line)
    _l_(4854)
    if match:
        _l_(4858)

        first_non_whitespace_idx = match.start(1)
        _l_(4855)

        lines.append(
            line[:first_non_whitespace_idx].expandtabs()
            + line[first_non_whitespace_idx:]
        )
        _l_(4856)
    else:
        lines.append(line)
        _l_(4857)
aux = lines
_l_(4860)
exit(aux)
