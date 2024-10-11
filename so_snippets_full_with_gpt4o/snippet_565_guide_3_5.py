class MockIter:# pragma: no cover
    def __init__(self, iterable):# pragma: no cover
        self._iter = iter(iterable)# pragma: no cover
    def next(self):# pragma: no cover
        return next(self._iter) # pragma: no cover
y = MockIter([1, 2, 3, 4]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9884132/what-are-iterator-iterable-and-iteration
from l3.Runtime import _l_
x=[1,2,3,4]
_l_(12928)

y=iter(x)
_l_(12929)

y=[1,2,3,4]
_l_(12930)

y.next()
_l_(12931)
1
_l_(12932)
y.next()
_l_(12933)
2
_l_(12934)
y.next()
_l_(12935)
3
_l_(12936)
y.next()
_l_(12937)
4
_l_(12938)
y.next()
_l_(12939)
StopIteration
_l_(12940)

