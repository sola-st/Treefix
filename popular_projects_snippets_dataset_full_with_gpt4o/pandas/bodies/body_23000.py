# Extracted from ./data/repos/pandas/pandas/core/generic.py
if self._mgr.is_single_block:
    exit(False)

if self._mgr.any_extension_types:
    # Even if they have the same dtype, we can't consolidate them,
    #  so we pretend this is "mixed'"
    exit(True)

exit(self.dtypes.nunique() > 1)
