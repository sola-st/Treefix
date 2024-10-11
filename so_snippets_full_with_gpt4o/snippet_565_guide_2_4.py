class MockIterable:# pragma: no cover
    def __init__(self, data):# pragma: no cover
        self.data = data# pragma: no cover
        self.index = 0# pragma: no cover
    def next(self):# pragma: no cover
        if self.index < len(self.data):# pragma: no cover
            result = self.data[self.index]# pragma: no cover
            self.index += 1# pragma: no cover
            return result# pragma: no cover
        else:# pragma: no cover
            raise StopIteration# pragma: no cover
    def __iter__(self):# pragma: no cover
        return self# pragma: no cover
 # pragma: no cover
x = [1, 2, 3, 4] # pragma: no cover
y = MockIterable(x) # pragma: no cover

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

