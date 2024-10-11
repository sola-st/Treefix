# Correcting the index access to avoid IndexError # pragma: no cover
def reverse(seq): # pragma: no cover
    for x in range(len(seq) - 1, -1, -1): # pragma: no cover
        yield seq[x] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards
from l3.Runtime import _l_
def reverse(seq):
    _l_(15205)

    for x in range(len(seq), -1, -1):
        _l_(15204)

        yield seq[x] #Yield a value to the generator
        _l_(15203) #Yield a value to the generator

for x in reverse([1, 2, 3]):
    _l_(15207)

    print(x)
    _l_(15206)

l = list(reverse([1, 2, 3]))
_l_(15208)

