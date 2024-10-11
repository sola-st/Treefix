import re # pragma: no cover
from typing import List # pragma: no cover
import token # pragma: no cover

class ProtoComment: # pragma: no cover
    def __init__(self, type, value, newlines, consumed): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
        self.newlines = newlines # pragma: no cover
        self.consumed = consumed # pragma: no cover
 # pragma: no cover
def make_comment(line, preview=None): # pragma: no cover
    return line.strip() # pragma: no cover
 # pragma: no cover
STANDALONE_COMMENT = 'STANDALONE_COMMENT' # pragma: no cover
token.COMMENT = 'COMMENT' # pragma: no cover
is_endmarker = False # pragma: no cover
preview = None # pragma: no cover
prefix = 'Line without comment\nLine without comment\n# This is a comment\nAnother text line' # pragma: no cover
aux = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Return a list of :class:`ProtoComment` objects parsed from the given `prefix`."""
result: List[ProtoComment] = []
_l_(18044)
if not prefix or "#" not in prefix:
    _l_(18046)

    aux = result
    _l_(18045)
    exit(aux)

consumed = 0
_l_(18047)
nlines = 0
_l_(18048)
ignored_lines = 0
_l_(18049)
for index, line in enumerate(re.split("\r?\n", prefix)):
    _l_(18064)

    consumed += len(line) + 1  # adding the length of the split '\n'
    _l_(18050)  # adding the length of the split '\n'
    line = line.lstrip()
    _l_(18051)
    if not line:
        _l_(18053)

        nlines += 1
        _l_(18052)
    if not line.startswith("#"):
        _l_(18057)

        # Escaped newlines outside of a comment are not really newlines at
        # all. We treat a single-line comment following an escaped newline
        # as a simple trailing comment.
        if line.endswith("\\"):
            _l_(18055)

            ignored_lines += 1
            _l_(18054)
        continue
        _l_(18056)

    if index == ignored_lines and not is_endmarker:
        _l_(18060)

        comment_type = token.COMMENT  # simple trailing comment
        _l_(18058)  # simple trailing comment
    else:
        comment_type = STANDALONE_COMMENT
        _l_(18059)
    comment = make_comment(line, preview=preview)
    _l_(18061)
    result.append(
        ProtoComment(
            type=comment_type, value=comment, newlines=nlines, consumed=consumed
        )
    )
    _l_(18062)
    nlines = 0
    _l_(18063)
aux = result
_l_(18065)
exit(aux)
