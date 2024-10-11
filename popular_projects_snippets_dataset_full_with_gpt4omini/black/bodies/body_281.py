# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return the first leaf that precedes `node`, if any."""
while node:
    _l_(4870)

    res = node.prev_sibling
    _l_(4861)
    if res:
        _l_(4868)

        if isinstance(res, Leaf):
            _l_(4863)

            aux = res
            _l_(4862)
            exit(aux)

        try:
            _l_(4867)

            aux = list(res.leaves())[-1]
            _l_(4864)
            exit(aux)

        except IndexError:
            _l_(4866)

            aux = None
            _l_(4865)
            exit(aux)

    node = node.parent
    _l_(4869)
aux = None
_l_(4871)
exit(aux)
