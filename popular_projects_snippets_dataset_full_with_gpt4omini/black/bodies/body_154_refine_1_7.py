import token # pragma: no cover
from typing import Dict, List # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.leaves = [{'type': token.COMMA}, {'type': token.RPAR, 'value': None}] # pragma: no cover
self.comments = {id(self.leaves[-1]): ['# comment', 'type: int']}  # Example comments dictionary # pragma: no cover
def is_type_comment(comment: str, flag: str = '') -> bool: return 'type' in comment # pragma: no cover

import token # pragma: no cover
from typing import Dict, List # pragma: no cover

class Leaf:  # A mock class to represent leaves # pragma: no cover
    def __init__(self, type, value=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.leaves = [Leaf(token.COMMA), Leaf(token.RPAR, None)] # pragma: no cover
self.comments = {id(self.leaves[-1]): ['# comment', 'type: int']}  # Example comments dictionary # pragma: no cover
def is_type_comment(comment: str, flag: str = '') -> bool: return 'type' in comment # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
ignored_ids = set()
_l_(7071)
try:
    _l_(7079)

    last_leaf = self.leaves[-1]
    _l_(7072)
    ignored_ids.add(id(last_leaf))
    _l_(7073)
    if last_leaf.type == token.COMMA or (
        last_leaf.type == token.RPAR and not last_leaf.value
    ):
        _l_(7076)

        # When trailing commas or optional parens are inserted by Black for
        # consistency, comments after the previous last element are not moved
        # (they don't have to, rendering will still be correct).  So we ignore
        # trailing commas and invisible.
        last_leaf = self.leaves[-2]
        _l_(7074)
        ignored_ids.add(id(last_leaf))
        _l_(7075)
except IndexError:
    _l_(7078)

    aux = False
    _l_(7077)
    exit(aux)

# A type comment is uncollapsable if it is attached to a leaf
# that isn't at the end of the line (since that could cause it
# to get associated to a different argument) or if there are
# comments before it (since that could cause it to get hidden
# behind a comment.
comment_seen = False
_l_(7080)
for leaf_id, comments in self.comments.items():
    _l_(7086)

    for comment in comments:
        _l_(7085)

        if is_type_comment(comment):
            _l_(7083)

            if comment_seen or (
                not is_type_comment(comment, " ignore")
                and leaf_id not in ignored_ids
            ):
                _l_(7082)

                aux = True
                _l_(7081)
                exit(aux)

        comment_seen = True
        _l_(7084)
aux = False
_l_(7087)

exit(aux)
