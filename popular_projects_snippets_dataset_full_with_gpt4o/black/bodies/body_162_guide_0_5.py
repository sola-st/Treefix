from typing import Sequence, Iterator, Tuple, Callable, List # pragma: no cover
from typing import cast # pragma: no cover

reversed = False # pragma: no cover
Leaf = type('Leaf', (object,), {'__init__': lambda self, prefix, value: setattr(self, 'prefix', prefix) or setattr(self, 'value', value) or None}) # pragma: no cover
MockTree = type('MockTree', (object,), {'__init__': lambda self, leaves: setattr(self, 'leaves', leaves) or None, 'comments_after': lambda self, leaf: []}) # pragma: no cover
enumerate_reversed = lambda leaves: reversed(list(enumerate(leaves))) # pragma: no cover
self = MockTree([Leaf('prefix1', 'value1'), Leaf('prefix2', 'value2\nvalue3')]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Return an enumeration of leaves with their length.

        Stops prematurely on multiline strings and standalone comments.
        """
op = cast(
    Callable[[Sequence[Leaf]], Iterator[Tuple[Index, Leaf]]],
    enumerate_reversed if reversed else enumerate,
)
_l_(16182)
for index, leaf in op(self.leaves):
    _l_(16189)

    length = len(leaf.prefix) + len(leaf.value)
    _l_(16183)
    if "\n" in leaf.value:
        _l_(16185)

        exit()  # Multiline strings, we can't continue.
        _l_(16184)  # Multiline strings, we can't continue.

    for comment in self.comments_after(leaf):
        _l_(16187)

        length += len(comment.value)
        _l_(16186)
    aux = (index, leaf, length)
    _l_(16188)

    exit(aux)
