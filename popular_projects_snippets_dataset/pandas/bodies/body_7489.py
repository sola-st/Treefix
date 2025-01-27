# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH#25169
mi1 = MultiIndex(levels=levels1, codes=codes1, names=names)
mi2 = MultiIndex(levels=levels2, codes=codes2, names=names)
mi_int = mi1.intersection(mi2)
assert mi_int._lexsort_depth == 2
