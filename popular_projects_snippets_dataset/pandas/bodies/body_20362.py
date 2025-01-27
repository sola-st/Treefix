# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
# In some cases we can retain RangeIndex, see also
#  DatetimeTimedeltaMixin._get_delete_Freq
if is_integer(loc):
    if loc in (0, -len(self)):
        exit(self[1:])
    if loc in (-1, len(self) - 1):
        exit(self[:-1])
    if len(self) == 3 and loc in (1, -2):
        exit(self[::2])

elif lib.is_list_like(loc):
    slc = lib.maybe_indices_to_slice(np.asarray(loc, dtype=np.intp), len(self))

    if isinstance(slc, slice):
        # defer to RangeIndex._difference, which is optimized to return
        #  a RangeIndex whenever possible
        other = self[slc]
        exit(self.difference(other, sort=False))

exit(super().delete(loc))
