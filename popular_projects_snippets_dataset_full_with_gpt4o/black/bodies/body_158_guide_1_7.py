import token # pragma: no cover

MockLeaf = type('MockLeaf', (object,), {'type': token.RPAR, 'value': '', 'parent': type('MockParent', (object,), {'leaves': lambda: [1, 2, 3] })()}) # pragma: no cover
MockComment = type('MockComment', (object,), {'type': 'STANDALONE_COMMENT', 'prefix': ''}) # pragma: no cover
MockBracketTracker = type('MockBracketTracker', (object,), {'any_open_brackets': lambda: True}) # pragma: no cover
comment = MockComment # pragma: no cover
self = type('MockSelf', (object,), {'bracket_tracker': MockBracketTracker(), 'leaves': [MockLeaf], 'comments': {}})() # pragma: no cover
STANDALONE_COMMENT = 'STANDALONE_COMMENT' # pragma: no cover
def is_type_comment(comment): return False # pragma: no cover
aux = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Add an inline or standalone comment to the line."""
if (
    comment.type == STANDALONE_COMMENT
    and self.bracket_tracker.any_open_brackets()
):
    _l_(19569)

    comment.prefix = ""
    _l_(19567)
    aux = False
    _l_(19568)
    exit(aux)

if comment.type != token.COMMENT:
    _l_(19571)

    aux = False
    _l_(19570)
    exit(aux)

if not self.leaves:
    _l_(19575)

    comment.type = STANDALONE_COMMENT
    _l_(19572)
    comment.prefix = ""
    _l_(19573)
    aux = False
    _l_(19574)
    exit(aux)

last_leaf = self.leaves[-1]
_l_(19576)
if (
    last_leaf.type == token.RPAR
    and not last_leaf.value
    and last_leaf.parent
    and len(list(last_leaf.parent.leaves())) <= 3
    and not is_type_comment(comment)
):
    _l_(19582)

    # Comments on an optional parens wrapping a single leaf should belong to
    # the wrapped node except if it's a type comment. Pinning the comment like
    # this avoids unstable formatting caused by comment migration.
    if len(self.leaves) < 2:
        _l_(19580)

        comment.type = STANDALONE_COMMENT
        _l_(19577)
        comment.prefix = ""
        _l_(19578)
        aux = False
        _l_(19579)
        exit(aux)

    last_leaf = self.leaves[-2]
    _l_(19581)
self.comments.setdefault(id(last_leaf), []).append(comment)
_l_(19583)
aux = True
_l_(19584)
exit(aux)
