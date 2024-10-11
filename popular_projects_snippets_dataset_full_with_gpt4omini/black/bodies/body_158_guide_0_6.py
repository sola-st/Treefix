import token # pragma: no cover
from typing import List # pragma: no cover

class MockLeaf: pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Add an inline or standalone comment to the line."""
if (
    comment.type == STANDALONE_COMMENT
    and self.bracket_tracker.any_open_brackets()
):
    _l_(8129)

    comment.prefix = ""
    _l_(8127)
    aux = False
    _l_(8128)
    exit(aux)

if comment.type != token.COMMENT:
    _l_(8131)

    aux = False
    _l_(8130)
    exit(aux)

if not self.leaves:
    _l_(8135)

    comment.type = STANDALONE_COMMENT
    _l_(8132)
    comment.prefix = ""
    _l_(8133)
    aux = False
    _l_(8134)
    exit(aux)

last_leaf = self.leaves[-1]
_l_(8136)
if (
    last_leaf.type == token.RPAR
    and not last_leaf.value
    and last_leaf.parent
    and len(list(last_leaf.parent.leaves())) <= 3
    and not is_type_comment(comment)
):
    _l_(8142)

    # Comments on an optional parens wrapping a single leaf should belong to
    # the wrapped node except if it's a type comment. Pinning the comment like
    # this avoids unstable formatting caused by comment migration.
    if len(self.leaves) < 2:
        _l_(8140)

        comment.type = STANDALONE_COMMENT
        _l_(8137)
        comment.prefix = ""
        _l_(8138)
        aux = False
        _l_(8139)
        exit(aux)

    last_leaf = self.leaves[-2]
    _l_(8141)
self.comments.setdefault(id(last_leaf), []).append(comment)
_l_(8143)
aux = True
_l_(8144)
exit(aux)
