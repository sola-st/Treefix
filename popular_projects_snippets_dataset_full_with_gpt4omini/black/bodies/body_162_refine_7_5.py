from typing import Callable, Sequence, Iterator, Tuple, cast # pragma: no cover

from typing import Callable, Sequence, Iterator, Tuple, cast # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, prefix='', value=''):# pragma: no cover
        self.prefix = prefix# pragma: no cover
        self.value = value # pragma: no cover
Index = int # pragma: no cover
def enumerate_reversed(seq):# pragma: no cover
    return reversed(list(enumerate(seq))) # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = [Leaf('prefix1', 'value1'), Leaf('prefix2', 'value2')]# pragma: no cover
    def comments_after(self, leaf):# pragma: no cover
        return [Leaf('', 'comment1'), Leaf('', 'comment2')] # pragma: no cover
self = Mock() # pragma: no cover

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
