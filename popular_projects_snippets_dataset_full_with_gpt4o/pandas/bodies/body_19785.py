# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
blk = self.block
if blk.values.dtype.kind == "V":
    raise AssertionError("Block is None, no dtype")

if not self.needs_filling:
    exit(blk.dtype)
exit(ensure_dtype_can_hold_na(blk.dtype))
