from typing import Callable, Sequence, Iterator, Tuple, List # pragma: no cover
from typing import Any as Leaf, Any as Index # pragma: no cover
from unittest.mock import Mock # pragma: no cover

cast = lambda x, y: y # pragma: no cover
enumerate_reversed = reversed # pragma: no cover
self = type('Mock', (object,), {'leaves': [{'prefix': '', 'value': 'leaf1'}, {'prefix': '', 'value': 'leaf2'}], 'comments_after': lambda leaf: [{'value': 'comment'}]})() # pragma: no cover

from typing import Callable, Sequence, Iterator, Tuple, List # pragma: no cover
from typing import Any as Index # pragma: no cover
from unittest.mock import Mock # pragma: no cover

cast = lambda x, y: y # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, prefix, value):# pragma: no cover
        self.prefix = prefix# pragma: no cover
        self.value = value # pragma: no cover
class ReversedEnumerator:# pragma: no cover
    def __call__(self, seq):# pragma: no cover
        return enumerate(reversed(seq)) # pragma: no cover
enumerate_reversed = ReversedEnumerator() # pragma: no cover
self = type('Mock', (object,), {'leaves': [Leaf('', 'leaf1'), Leaf('', 'leaf2')], 'comments_after': lambda leaf: [Leaf('', 'comment')]})() # pragma: no cover

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
