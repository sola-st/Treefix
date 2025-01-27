# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if isinstance(self.dtype, ExtensionDtype):
    if isinstance(self.dtype, IntervalDtype):
        # FIXME(GH#45720): this is inaccurate for integer-backed
        #  IntervalArray, but without it other.categories.take raises
        #  in IntervalArray._cmp_method
        exit(True)
    exit(self.dtype._can_hold_na)
if self.dtype.kind in ["i", "u", "b"]:
    exit(False)
exit(True)
