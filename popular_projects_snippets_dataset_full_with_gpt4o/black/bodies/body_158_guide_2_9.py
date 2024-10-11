import token # pragma: no cover

class MockBracketTracker: # pragma: no cover
    def any_open_brackets(self): # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
class MockComment: # pragma: no cover
    def __init__(self, type, prefix=''): # pragma: no cover
        self.type = type # pragma: no cover
        self.prefix = prefix # pragma: no cover
 # pragma: no cover
class MockLeaf: # pragma: no cover
    def __init__(self, type, value, parent=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
        self.parent = parent # pragma: no cover
    def leaves(self): # pragma: no cover
        return [self] # pragma: no cover
 # pragma: no cover
class MockParent: # pragma: no cover
    def leaves(self): # pragma: no cover
        return [1, 2, 3] # pragma: no cover
 # pragma: no cover
def is_type_comment(comment): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
STANDALONE_COMMENT = 'STANDALONE_COMMENT' # pragma: no cover
comment = MockComment(STANDALONE_COMMENT) # pragma: no cover
last_leaf_parent = MockParent() # pragma: no cover
last_leaf = MockLeaf(token.RPAR, '', last_leaf_parent) # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'bracket_tracker': MockBracketTracker(), # pragma: no cover
    'leaves': [last_leaf], # pragma: no cover
    'comments': {} # pragma: no cover
}) # pragma: no cover

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
