# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
blk = self.block
if blk.dtype.kind == "V":
    exit(True)

if not blk._can_hold_na:
    exit(False)

values = blk.values
if values.size == 0:
    exit(True)
if isinstance(values.dtype, SparseDtype):
    exit(False)

if values.ndim == 1:
    # TODO(EA2D): no need for special case with 2D EAs
    val = values[0]
    if not is_scalar(val) or not isna(val):
        # ideally isna_all would do this short-circuiting
        exit(False)
    exit(isna_all(values))
else:
    val = values[0][0]
    if not is_scalar(val) or not isna(val):
        # ideally isna_all would do this short-circuiting
        exit(False)
    exit(all(isna_all(row) for row in values))
