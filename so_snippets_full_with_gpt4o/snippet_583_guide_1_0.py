import collections # pragma: no cover

orig = {'A': 1, 'B': 2, 'C': 3} # pragma: no cover
extra = {'A': 3, 'B': 2, 'C': 3} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8930915/append-a-dictionary-to-a-dictionary
from l3.Runtime import _l_
orig.update(extra)    # Python 2.7+
_l_(14194)    # Python 2.7+
orig |= extra         # Python 3.9+
_l_(14195)         # Python 3.9+

# Python 2.7+
dest = collections.ChainMap(orig, extra)
_l_(14196)
dest = {k: v for d in (orig, extra) for (k, v) in d.items()}
_l_(14197)

# Python 3
dest = {**orig, **extra}          
_l_(14198)          
dest = {**orig, 'D': 4, 'E': 5}
_l_(14199)

# Python 3.9+ 
dest = orig | extra
_l_(14200)

orig  = {'A': 1, 'B': 2}
_l_(14201)
extra = {'A': 3, 'C': 3}
_l_(14202)

dest = orig | extra
_l_(14203)
# dest = {'A': 3, 'B': 2, 'C': 3}

dest = extra | orig
_l_(14204)
# dest = {'A': 1, 'B': 2, 'C': 3}

