class MockIterator: # pragma: no cover
    def __init__(self, data): # pragma: no cover
        self.data = data # pragma: no cover
        self.index = 0 # pragma: no cover
    def __iter__(self): # pragma: no cover
        return self # pragma: no cover
    def next(self): # pragma: no cover
        if self.index < len(self.data): # pragma: no cover
            value = self.data[self.index] # pragma: no cover
            self.index += 1 # pragma: no cover
            return value # pragma: no cover
        else: # pragma: no cover
            raise StopIteration # pragma: no cover
x = [1, 2, 3, 4] # pragma: no cover
y = MockIterator(x) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9884132/what-are-iterator-iterable-and-iteration
from l3.Runtime import _l_
x=[1,2,3,4]
_l_(1018)

y=iter(x)
_l_(1019)

y=[1,2,3,4]
_l_(1020)

y.next()
_l_(1021)
1
_l_(1022)
y.next()
_l_(1023)
2
_l_(1024)
y.next()
_l_(1025)
3
_l_(1026)
y.next()
_l_(1027)
4
_l_(1028)
y.next()
_l_(1029)
StopIteration
_l_(1030)

