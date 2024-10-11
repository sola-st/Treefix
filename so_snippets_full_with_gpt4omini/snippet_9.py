# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
from l3.Runtime import _l_
xs = [8, 23, 45]
_l_(659)
for i in range(len(xs)):
    _l_(661)

    print("item #{} = {}".format(i + 1, xs[i]))
    _l_(660)

xs = [8, 23, 45]
_l_(662)
for idx, val in enumerate(xs, start=1):
    _l_(664)

    print("item #{} = {}".format(idx, val))
    _l_(663)

