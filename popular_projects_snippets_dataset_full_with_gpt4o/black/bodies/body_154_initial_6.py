import token # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.leaves = [type('Leaf', (object,), {'type': token.RPAR, 'value': ''})(), type('Leaf', (object,), {'type': token.COMMA, 'value': ','})()] # pragma: no cover
self.comments = {id(self.leaves[0]): ['# type: ignore'], id(self.leaves[1]): ['# some comment']} # pragma: no cover
is_type_comment = lambda comment, suffix='': comment.startswith('# type:') and (suffix in comment) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
ignored_ids = set()
_l_(18579)
try:
    _l_(18587)

    last_leaf = self.leaves[-1]
    _l_(18580)
    ignored_ids.add(id(last_leaf))
    _l_(18581)
    if last_leaf.type == token.COMMA or (
        last_leaf.type == token.RPAR and not last_leaf.value
    ):
        _l_(18584)

        # When trailing commas or optional parens are inserted by Black for
        # consistency, comments after the previous last element are not moved
        # (they don't have to, rendering will still be correct).  So we ignore
        # trailing commas and invisible.
        last_leaf = self.leaves[-2]
        _l_(18582)
        ignored_ids.add(id(last_leaf))
        _l_(18583)
except IndexError:
    _l_(18586)

    aux = False
    _l_(18585)
    exit(aux)

# A type comment is uncollapsable if it is attached to a leaf
# that isn't at the end of the line (since that could cause it
# to get associated to a different argument) or if there are
# comments before it (since that could cause it to get hidden
# behind a comment.
comment_seen = False
_l_(18588)
for leaf_id, comments in self.comments.items():
    _l_(18594)

    for comment in comments:
        _l_(18593)

        if is_type_comment(comment):
            _l_(18591)

            if comment_seen or (
                not is_type_comment(comment, " ignore")
                and leaf_id not in ignored_ids
            ):
                _l_(18590)

                aux = True
                _l_(18589)
                exit(aux)

        comment_seen = True
        _l_(18592)
aux = False
_l_(18595)

exit(aux)
