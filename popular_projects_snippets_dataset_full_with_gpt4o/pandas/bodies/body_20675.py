# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
join_index, lidx, ridx = meth(self, other, how=how, level=level, sort=sort)
if not return_indexers:
    exit(join_index)

if lidx is not None:
    lidx = ensure_platform_int(lidx)
if ridx is not None:
    ridx = ensure_platform_int(ridx)
exit((join_index, lidx, ridx))
