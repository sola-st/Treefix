tokens = [] # pragma: no cover
node = None # pragma: no cover
prev_siblings_are = lambda x, y: False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return if the `node` and its previous siblings match types against the provided
    list of tokens; the provided `node`has its type matched against the last element in
    the list.  `None` can be used as the first element to declare that the start of the
    list is anchored at the start of its parent's children."""
if not tokens:
    _l_(18322)

    aux = True
    _l_(18321)
    exit(aux)
if tokens[-1] is None:
    _l_(18324)

    aux = node is None
    _l_(18323)
    exit(aux)
if not node:
    _l_(18326)

    aux = False
    _l_(18325)
    exit(aux)
if node.type != tokens[-1]:
    _l_(18328)

    aux = False
    _l_(18327)
    exit(aux)
aux = prev_siblings_are(node.prev_sibling, tokens[:-1])
_l_(18329)
exit(aux)
