bigdict = {'a': 1, 'b': 2, 'c': 3, 'l': 4, 'm': 5, 'n': 6, 'o': 7} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5352546/extract-a-subset-of-key-value-pairs-from-dictionary
from l3.Runtime import _l_
{k: bigdict[k] for k in bigdict.keys() if k not in ['l', 'm', 'n']}
_l_(1818)

