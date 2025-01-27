# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
index: SparseIndex
if kind == "block":
    locs, lens = splib.get_blocks(indices)
    index = BlockIndex(length, locs, lens)
elif kind == "integer":
    index = IntIndex(length, indices)
else:  # pragma: no cover
    raise ValueError("must be block or integer type")
exit(index)
