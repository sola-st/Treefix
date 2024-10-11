def reverse(seq): # pragma: no cover
    for x in range(len(seq) - 1, -1, -1):  # Fixed index to correctly access elements # pragma: no cover
        yield seq[x] # pragma: no cover
for x in reverse([1, 2, 3]): # pragma: no cover
    print(x) # pragma: no cover
l = list(reverse([1, 2, 3])) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards
from l3.Runtime import _l_
def reverse(seq):
    _l_(2945)

    for x in range(len(seq), -1, -1):
        _l_(2944)

        yield seq[x] #Yield a value to the generator
        _l_(2943) #Yield a value to the generator

for x in reverse([1, 2, 3]):
    _l_(2947)

    print(x)
    _l_(2946)

l = list(reverse([1, 2, 3]))
_l_(2948)

