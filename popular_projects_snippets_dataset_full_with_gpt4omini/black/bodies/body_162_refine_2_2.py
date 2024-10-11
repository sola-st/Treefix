from typing import Callable, Sequence, Iterator, Tuple # pragma: no cover
from typing_extensions import Literal # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, prefix: str, value: str):# pragma: no cover
        self.prefix = prefix# pragma: no cover
        self.value = value # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = [Leaf('prefix1', 'value1'), Leaf('prefix2', 'value2')]  # Sample leaves# pragma: no cover
    def comments_after(self, leaf: Leaf):# pragma: no cover
        return [Leaf('comment_prefix', 'comment_value')]  # Sample comments# pragma: no cover
self = Mock() # pragma: no cover
Index = int # pragma: no cover
enumerate_reversed = False # pragma: no cover
cast = lambda x, y: x # pragma: no cover

from typing import Callable, Sequence, Iterator, Tuple, cast # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, prefix: str, value: str):# pragma: no cover
        self.prefix = prefix# pragma: no cover
        self.value = value # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = [Leaf('prefix1', 'value1'), Leaf('prefix2', 'value2')]# pragma: no cover
    def comments_after(self, leaf: Leaf):# pragma: no cover
        return [Leaf('comment_prefix', 'comment_value')] # pragma: no cover
self = Mock() # pragma: no cover
Index = int # pragma: no cover
enumerate_reversed = False # pragma: no cover
def enumerate_reversed(seq):# pragma: no cover
    return reversed(list(enumerate(seq))) # pragma: no cover

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
