from typing import Callable, Sequence, Iterator, Tuple, cast # pragma: no cover
from collections import namedtuple # pragma: no cover

Leaf = namedtuple('Leaf', ['prefix', 'value']) # pragma: no cover
Index = int # pragma: no cover
enumerate_reversed = lambda seq: reversed(list(enumerate(seq))) # pragma: no cover

from typing import Callable, Sequence, Iterator, Tuple, cast # pragma: no cover
from collections import namedtuple # pragma: no cover

Leaf = namedtuple('Leaf', ['prefix', 'value']) # pragma: no cover
Index = int # pragma: no cover
enumerate_reversed = lambda seq: reversed(list(enumerate(seq))) # pragma: no cover
mock_instance = type('Mock', (object,), {'leaves': [Leaf(prefix='', value='leaf1'), Leaf(prefix=' ', value='leaf2')], 'comments_after': lambda self, leaf: [Leaf(prefix='', value='# comment')]})() # pragma: no cover
self = mock_instance # pragma: no cover

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
