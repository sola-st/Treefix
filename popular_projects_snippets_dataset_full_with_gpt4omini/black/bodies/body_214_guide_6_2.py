from typing import List # pragma: no cover
import re # pragma: no cover
class ProtoComment: # pragma: no cover
    def __init__(self, type, value, newlines, consumed): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
        self.newlines = newlines # pragma: no cover
        self.consumed = consumed # pragma: no cover
class token: # pragma: no cover
    COMMENT = 'comment' # pragma: no cover
    STANDALONE_COMMENT = 'standalone' # pragma: no cover
def make_comment(line, preview=None): return line.strip() # pragma: no cover

prefix = 'Normal line without comments.' # pragma: no cover
preview = None # pragma: no cover
is_endmarker = False # pragma: no cover
result = [] # pragma: no cover
ignored_lines = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Return a list of :class:`ProtoComment` objects parsed from the given `prefix`."""
result: List[ProtoComment] = []
_l_(6783)
if not prefix or "#" not in prefix:
    _l_(6785)

    aux = result
    _l_(6784)
    exit(aux)

consumed = 0
_l_(6786)
nlines = 0
_l_(6787)
ignored_lines = 0
_l_(6788)
for index, line in enumerate(re.split("\r?\n", prefix)):
    _l_(6803)

    consumed += len(line) + 1  # adding the length of the split '\n'
    _l_(6789)  # adding the length of the split '\n'
    line = line.lstrip()
    _l_(6790)
    if not line:
        _l_(6792)

        nlines += 1
        _l_(6791)
    if not line.startswith("#"):
        _l_(6796)

        # Escaped newlines outside of a comment are not really newlines at
        # all. We treat a single-line comment following an escaped newline
        # as a simple trailing comment.
        if line.endswith("\\"):
            _l_(6794)

            ignored_lines += 1
            _l_(6793)
        continue
        _l_(6795)

    if index == ignored_lines and not is_endmarker:
        _l_(6799)

        comment_type = token.COMMENT  # simple trailing comment
        _l_(6797)  # simple trailing comment
    else:
        comment_type = STANDALONE_COMMENT
        _l_(6798)
    comment = make_comment(line, preview=preview)
    _l_(6800)
    result.append(
        ProtoComment(
            type=comment_type, value=comment, newlines=nlines, consumed=consumed
        )
    )
    _l_(6801)
    nlines = 0
    _l_(6802)
aux = result
_l_(6804)
exit(aux)
