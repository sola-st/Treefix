import collections # pragma: no cover

orig = {'A': 1, 'B': 2} # pragma: no cover
extra = {'A': 3, 'C': 3} # pragma: no cover
collections = type('Mock', (object,), {'ChainMap': collections.ChainMap}) # pragma: no cover

import collections # pragma: no cover

orig = {'A': 1, 'B': 2} # pragma: no cover
extra = {'A': 3, 'C': 3} # pragma: no cover
collections = type('Mock', (object,), {'ChainMap': collections.ChainMap})() # pragma: no cover
orig = dict(orig)  # Ensures orig is an instance of dict # pragma: no cover
extra = dict(extra)  # Ensures extra is an instance of dict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8930915/append-a-dictionary-to-a-dictionary
from l3.Runtime import _l_
orig.update(extra)    # Python 2.7+
_l_(1979)    # Python 2.7+
orig |= extra         # Python 3.9+
_l_(1980)         # Python 3.9+

# Python 2.7+
dest = collections.ChainMap(orig, extra)
_l_(1981)
dest = {k: v for d in (orig, extra) for (k, v) in d.items()}
_l_(1982)

# Python 3
dest = {**orig, **extra}          
_l_(1983)          
dest = {**orig, 'D': 4, 'E': 5}
_l_(1984)

# Python 3.9+ 
dest = orig | extra
_l_(1985)

orig  = {'A': 1, 'B': 2}
_l_(1986)
extra = {'A': 3, 'C': 3}
_l_(1987)

dest = orig | extra
_l_(1988)
# dest = {'A': 3, 'B': 2, 'C': 3}

dest = extra | orig
_l_(1989)
# dest = {'A': 1, 'B': 2, 'C': 3}

