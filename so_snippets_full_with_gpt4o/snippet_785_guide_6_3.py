from __future__ import annotations # pragma: no cover
from typing import Generic, List, Optional, TypeVar # pragma: no cover
from heapq import heapify, heappop, heappush, heapreplace # pragma: no cover

types = type('types', (object,), {'ModuleType': type(sys)}) # pragma: no cover
doctest = types.ModuleType('doctest') # pragma: no cover
def testmod(): print('doctest executed') # pragma: no cover
doctest.testmod = testmod # pragma: no cover
sys.modules['doctest'] = doctest # pragma: no cover
doctest.testmod() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
from __future__ import annotations  # To allow "MinHeap.push -> MinHeap:"
from l3.Runtime import _l_
_l_(13419)  # To allow "MinHeap.push -> MinHeap:"
try:
    from typing import Generic, List, Optional, TypeVar
    _l_(13421)

except ImportError:
    pass
try:
    from heapq import heapify, heappop, heappush, heapreplace
    _l_(13423)

except ImportError:
    pass


T = TypeVar('T')
_l_(13424)


class MinHeap(Generic[T]):
    _l_(13448)

    '''
    MinHeap provides a nicer API around heapq's functionality.
    As it is a minimum heap, the first element of the heap is always the
    smallest.
    >>> h = MinHeap([3, 1, 4, 2])
    >>> h[0]
    1
    >>> h.peek()
    1
    >>> h.push(5)  # N.B.: the array isn't always fully sorted.
    [1, 2, 4, 3, 5]
    >>> h.pop()
    1
    >>> h.pop()
    2
    >>> h.pop()
    3
    >>> h.push(3).push(2)
    [2, 3, 4, 5]
    >>> h.replace(1)
    2
    >>> h
    [1, 3, 4, 5]
    '''
    _l_(13425)
    def __init__(self, array: Optional[List[T]] = None):
        _l_(13430)

        if array is None:
            _l_(13427)

            array = []
            _l_(13426)
        heapify(array)
        _l_(13428)
        self.h = array
        _l_(13429)
    def push(self, x: T) -> MinHeap:
        _l_(13433)

        heappush(self.h, x)
        _l_(13431)
        aux = self  # To allow chaining operations.
        _l_(13432)  # To allow chaining operations.
        return aux  # To allow chaining operations.
    def peek(self) -> T:
        _l_(13435)

        aux = self.h[0]
        _l_(13434)
        return aux
    def pop(self) -> T:
        _l_(13437)

        aux = heappop(self.h)
        _l_(13436)
        return aux
    def replace(self, x: T) -> T:
        _l_(13439)

        aux = heapreplace(self.h, x)
        _l_(13438)
        return aux
    def __getitem__(self, i) -> T:
        _l_(13441)

        aux = self.h[i]
        _l_(13440)
        return aux
    def __len__(self) -> int:
        _l_(13443)

        aux = len(self.h)
        _l_(13442)
        return aux
    def __str__(self) -> str:
        _l_(13445)

        aux = str(self.h)
        _l_(13444)
        return aux
    def __repr__(self) -> str:
        _l_(13447)

        aux = str(self.h)
        _l_(13446)
        return aux


class Reverse(Generic[T]):
    _l_(13468)

    '''
    Wrap around the provided object, reversing the comparison operators.
    >>> 1 < 2
    True
    >>> Reverse(1) < Reverse(2)
    False
    >>> Reverse(2) < Reverse(1)
    True
    >>> Reverse(1) <= Reverse(2)
    False
    >>> Reverse(2) <= Reverse(1)
    True
    >>> Reverse(2) <= Reverse(2)
    True
    >>> Reverse(1) == Reverse(1)
    True
    >>> Reverse(2) > Reverse(1)
    False
    >>> Reverse(1) > Reverse(2)
    True
    >>> Reverse(2) >= Reverse(1)
    False
    >>> Reverse(1) >= Reverse(2)
    True
    >>> Reverse(1)
    1
    '''
    _l_(13449)
    def __init__(self, x: T) -> None:
        _l_(13451)

        self.x = x
        _l_(13450)
    def __lt__(self, other: Reverse) -> bool:
        _l_(13453)

        aux = other.x.__lt__(self.x)
        _l_(13452)
        return aux
    def __le__(self, other: Reverse) -> bool:
        _l_(13455)

        aux = other.x.__le__(self.x)
        _l_(13454)
        return aux
    def __eq__(self, other) -> bool:
        _l_(13457)

        aux = self.x == other.x
        _l_(13456)
        return aux
    def __ne__(self, other: Reverse) -> bool:
        _l_(13459)

        aux = other.x.__ne__(self.x)
        _l_(13458)
        return aux
    def __ge__(self, other: Reverse) -> bool:
        _l_(13461)

        aux = other.x.__ge__(self.x)
        _l_(13460)
        return aux
    def __gt__(self, other: Reverse) -> bool:
        _l_(13463)

        aux = other.x.__gt__(self.x)
        _l_(13462)
        return aux
    def __str__(self):
        _l_(13465)

        aux = str(self.x)
        _l_(13464)
        return aux
    def __repr__(self):
        _l_(13467)

        aux = str(self.x)
        _l_(13466)
        return aux


class MaxHeap(MinHeap):
    _l_(13483)

    '''
    MaxHeap provides an implement of a maximum-heap, as heapq does not provide
    it. As it is a maximum heap, the first element of the heap is always the
    largest. It achieves this by wrapping around elements with Reverse,
    which reverses the comparison operations used by heapq.
    >>> h = MaxHeap([3, 1, 4, 2])
    >>> h[0]
    4
    >>> h.peek()
    4
    >>> h.push(5)  # N.B.: the array isn't always fully sorted.
    [5, 4, 3, 1, 2]
    >>> h.pop()
    5
    >>> h.pop()
    4
    >>> h.pop()
    3
    >>> h.pop()
    2
    >>> h.push(3).push(2).push(4)
    [4, 3, 2, 1]
    >>> h.replace(1)
    4
    >>> h
    [3, 1, 2, 1]
    '''
    _l_(13469)
    def __init__(self, array: Optional[List[T]] = None):
        _l_(13473)

        if array is not None:
            _l_(13471)

            array = [Reverse(x) for x in array]  # Wrap with Reverse.
            _l_(13470)  # Wrap with Reverse.
        super().__init__(array)
        _l_(13472)
    def push(self, x: T) -> MaxHeap:
        _l_(13476)

        super().push(Reverse(x))
        _l_(13474)
        aux = self
        _l_(13475)
        return aux
    def peek(self) -> T:
        _l_(13478)

        aux = super().peek().x
        _l_(13477)
        return aux
    def pop(self) -> T:
        _l_(13480)

        aux = super().pop().x
        _l_(13479)
        return aux
    def replace(self, x: T) -> T:
        _l_(13482)

        aux = super().replace(Reverse(x)).x
        _l_(13481)
        return aux


if __name__ == '__main__':
    _l_(13487)

    try:
        import doctest
        _l_(13485)

    except ImportError:
        pass
    doctest.testmod()
    _l_(13486)

