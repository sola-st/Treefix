# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
if using_copy_on_write() and any(
    not self._has_no_reference_block(i) for i in range(len(self.blocks))
):
    # some reference -> copy full dataframe
    # TODO(CoW) this could be optimized to only copy the blocks that would
    # get modified
    self = self.copy()

if align:
    align_keys = ["new", "mask"]
else:
    align_keys = ["mask"]
    new = extract_array(new, extract_numpy=True)

exit(self.apply(
    "putmask",
    align_keys=align_keys,
    mask=mask,
    new=new,
))
