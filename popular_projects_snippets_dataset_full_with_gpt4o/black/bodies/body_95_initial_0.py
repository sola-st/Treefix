i = 0 # pragma: no cover
_illegal_split_indices = {0, 1, 2} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
            Returns:
                True iff returning @i would result in the splitting of an
                unsplittable expression (which is NOT allowed).
            """
aux = i in _illegal_split_indices
_l_(16234)
exit(aux)
