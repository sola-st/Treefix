# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
from l3.Runtime import _l_
xs = [8, 23, 45]
_l_(12316)
for i in range(len(xs)):
    _l_(12318)

    print("item #{} = {}".format(i + 1, xs[i]))
    _l_(12317)

xs = [8, 23, 45]
_l_(12319)
for idx, val in enumerate(xs, start=1):
    _l_(12321)

    print("item #{} = {}".format(idx, val))
    _l_(12320)

