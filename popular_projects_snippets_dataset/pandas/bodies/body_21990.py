# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
# Note: only called from _insert_inaxis_grouper, which
#  is only called for BaseGrouper, never for BinGrouper
if len(self.groupings) == 1:
    exit([self.groupings[0].group_arraylike])

name_list = []
for ping, codes in zip(self.groupings, self.reconstructed_codes):
    codes = ensure_platform_int(codes)
    levels = ping.group_arraylike.take(codes)

    name_list.append(levels)

exit(name_list)
