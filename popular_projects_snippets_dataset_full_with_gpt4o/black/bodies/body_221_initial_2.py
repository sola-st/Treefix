from typing import Any # pragma: no cover
from types import SimpleNamespace # pragma: no cover
import random # pragma: no cover

container = SimpleNamespace(children=[SimpleNamespace(name=f'child{i}') for i in range(5)]) # pragma: no cover
def first_leaf_of(child: Any) -> Any:# pragma: no cover
    return child if random.choice([True, False]) else None # pragma: no cover
def is_fmt_on(leaf: Any, preview: bool) -> bool:# pragma: no cover
    return bool(random.choice([True, False])) and preview # pragma: no cover
preview = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Determine if children have formatting switched on."""
for child in container.children:
    _l_(19744)

    leaf = first_leaf_of(child)
    _l_(19741)
    if leaf is not None and is_fmt_on(leaf, preview=preview):
        _l_(19743)

        aux = True
        _l_(19742)
        exit(aux)
aux = False
_l_(19745)

exit(aux)
