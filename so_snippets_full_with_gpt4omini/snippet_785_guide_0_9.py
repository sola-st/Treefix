from heapq import heapify, heappop, heappush, heapreplace # pragma: no cover
from typing import Generic, List, Optional, TypeVar # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
from __future__ import annotations  # To allow "MinHeap.push -> MinHeap:"
from l3.Runtime import _l_
_l_(1206)  # To allow "MinHeap.push -> MinHeap:"
try:
    from typing import Generic, List, Optional, TypeVar
    _l_(1208)

except ImportError:
    pass
try:
    from heapq import heapify, heappop, heappush, heapreplace
    _l_(1210)

except ImportError:
    pass


T = TypeVar('T')
_l_(1211)


class MinHeap(Generic[T]):
    _l_(1235)

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
    _l_(1212)
    def __init__(self, array: Optional[List[T]] = None):
        _l_(1217)

        if array is None:
            _l_(1214)

            array = []
            _l_(1213)
        heapify(array)
        _l_(1215)
        self.h = array
        _l_(1216)
    def push(self, x: T) -> MinHeap:
        _l_(1220)

        heappush(self.h, x)
        _l_(1218)
        aux = self  # To allow chaining operations.
        _l_(1219)  # To allow chaining operations.
        return aux  # To allow chaining operations.
    def peek(self) -> T:
        _l_(1222)

        aux = self.h[0]
        _l_(1221)
        return aux
    def pop(self) -> T:
        _l_(1224)

        aux = heappop(self.h)
        _l_(1223)
        return aux
    def replace(self, x: T) -> T:
        _l_(1226)

        aux = heapreplace(self.h, x)
        _l_(1225)
        return aux
    def __getitem__(self, i) -> T:
        _l_(1228)

        aux = self.h[i]
        _l_(1227)
        return aux
    def __len__(self) -> int:
        _l_(1230)

        aux = len(self.h)
        _l_(1229)
        return aux
    def __str__(self) -> str:
        _l_(1232)

        aux = str(self.h)
        _l_(1231)
        return aux
    def __repr__(self) -> str:
        _l_(1234)

        aux = str(self.h)
        _l_(1233)
        return aux


class Reverse(Generic[T]):
    _l_(1255)

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
    _l_(1236)
    def __init__(self, x: T) -> None:
        _l_(1238)

        self.x = x
        _l_(1237)
    def __lt__(self, other: Reverse) -> bool:
        _l_(1240)

        aux = other.x.__lt__(self.x)
        _l_(1239)
        return aux
    def __le__(self, other: Reverse) -> bool:
        _l_(1242)

        aux = other.x.__le__(self.x)
        _l_(1241)
        return aux
    def __eq__(self, other) -> bool:
        _l_(1244)

        aux = self.x == other.x
        _l_(1243)
        return aux
    def __ne__(self, other: Reverse) -> bool:
        _l_(1246)

        aux = other.x.__ne__(self.x)
        _l_(1245)
        return aux
    def __ge__(self, other: Reverse) -> bool:
        _l_(1248)

        aux = other.x.__ge__(self.x)
        _l_(1247)
        return aux
    def __gt__(self, other: Reverse) -> bool:
        _l_(1250)

        aux = other.x.__gt__(self.x)
        _l_(1249)
        return aux
    def __str__(self):
        _l_(1252)

        aux = str(self.x)
        _l_(1251)
        return aux
    def __repr__(self):
        _l_(1254)

        aux = str(self.x)
        _l_(1253)
        return aux


class MaxHeap(MinHeap):
    _l_(1270)

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
    _l_(1256)
    def __init__(self, array: Optional[List[T]] = None):
        _l_(1260)

        if array is not None:
            _l_(1258)

            array = [Reverse(x) for x in array]  # Wrap with Reverse.
            _l_(1257)  # Wrap with Reverse.
        super().__init__(array)
        _l_(1259)
    def push(self, x: T) -> MaxHeap:
        _l_(1263)

        super().push(Reverse(x))
        _l_(1261)
        aux = self
        _l_(1262)
        return aux
    def peek(self) -> T:
        _l_(1265)

        aux = super().peek().x
        _l_(1264)
        return aux
    def pop(self) -> T:
        _l_(1267)

        aux = super().pop().x
        _l_(1266)
        return aux
    def replace(self, x: T) -> T:
        _l_(1269)

        aux = super().replace(Reverse(x)).x
        _l_(1268)
        return aux


if __name__ == '__main__':
    _l_(1274)

    try:
        import doctest
        _l_(1272)

    except ImportError:
        pass
    doctest.testmod()
    _l_(1273)

