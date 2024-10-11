import token # pragma: no cover
from typing import List, Dict # pragma: no cover

class MockComment:# pragma: no cover
    def __init__(self, comment_type):# pragma: no cover
        self.type = comment_type# pragma: no cover
        self.prefix = '' # pragma: no cover
class MockLeaf:# pragma: no cover
    def __init__(self, leaf_type, parent=None):# pragma: no cover
        self.type = leaf_type# pragma: no cover
        self.value = None# pragma: no cover
        self.parent = parent# pragma: no cover
    def leaves(self):# pragma: no cover
        return [self] if self.parent else [] # pragma: no cover
class MockParent:# pragma: no cover
    def leaves(self):# pragma: no cover
        return [MockLeaf(token.NAME) for _ in range(2)] # pragma: no cover
  # Provide at least two leaves for the parent # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def any_open_brackets(self):# pragma: no cover
        return True # pragma: no cover
class MockProcessor:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.bracket_tracker = MockBracketTracker()# pragma: no cover
        self.comments = {} # pragma: no cover
def is_type_comment(comment):# pragma: no cover
    return False # pragma: no cover
  # Mock function that returns False for type comments # pragma: no cover
self = MockProcessor() # pragma: no cover
comment = MockComment(token.COMMENT) # pragma: no cover
comment.type = 'STANDALONE_COMMENT' # pragma: no cover

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
