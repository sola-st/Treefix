from typing import Callable, Iterator, List, Tuple, Sequence, cast # pragma: no cover

Index = int # pragma: no cover
enumerate_reversed = lambda seq: reversed(list(enumerate(seq))) # pragma: no cover

from typing import Callable, Iterator, List, Tuple, Sequence, cast # pragma: no cover

Index = int # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, prefix: str, value: str):# pragma: no cover
        self.prefix = prefix# pragma: no cover
        self.value = value # pragma: no cover
def enumerate_reversed(seq: Sequence[Leaf]) -> Iterator[Tuple[Index, Leaf]]:# pragma: no cover
    return reversed(list(enumerate(seq))) # pragma: no cover
self = type('Mock', (), { 'leaves': [Leaf('test_prefix_1', 'test_value_1'), Leaf('test_prefix_2', 'test_value_2')], 'comments_after': lambda leaf: [Leaf('comment_prefix', 'comment_value')] })() # pragma: no cover
cast = lambda x, _: x # pragma: no cover

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
