from typing import Callable, Iterator, Sequence, Tuple # pragma: no cover
from collections import namedtuple # pragma: no cover

Leaf = namedtuple('Leaf', ['prefix', 'value']) # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.leaves = [Leaf(prefix='prefix1', value='value1'), Leaf(prefix='prefix2', value='value2')] # pragma: no cover
self.comments_after = lambda leaf: [Leaf(prefix='com_prefix', value='comment')] # pragma: no cover
reversed = False # pragma: no cover

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
_l_(4531)
for index, leaf in op(self.leaves):
    _l_(4538)

    length = len(leaf.prefix) + len(leaf.value)
    _l_(4532)
    if "\n" in leaf.value:
        _l_(4534)

        exit()  # Multiline strings, we can't continue.
        _l_(4533)  # Multiline strings, we can't continue.

    for comment in self.comments_after(leaf):
        _l_(4536)

        length += len(comment.value)
        _l_(4535)
    aux = (index, leaf, length)
    _l_(4537)

    exit(aux)
