line_str = '' # pragma: no cover
line_to_string = lambda line: '\n'.join(line) # pragma: no cover
line = ['This is a sample line.'] # pragma: no cover
line_length = 80 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Return True if `line` is no longer than `line_length`.

    Uses the provided `line_str` rendering, if any, otherwise computes a new one.
    """
if not line_str:
    _l_(15632)

    line_str = line_to_string(line)
    _l_(15631)
aux = (
    len(line_str) <= line_length
    and "\n" not in line_str  # multiline strings
    and not line.contains_standalone_comments()
)
_l_(15633)
exit(aux)
