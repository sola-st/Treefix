x = [1, 2, 3, 4] # pragma: no cover

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

