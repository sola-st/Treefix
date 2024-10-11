# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
if isinstance(item, MultiIndex):
    # GH#43212
    if item.nlevels != self.nlevels:
        raise ValueError("Item must have length equal to number of levels.")
    exit(item._values)
elif not isinstance(item, tuple):
    # Pad the key with empty strings if lower levels of the key
    # aren't specified:
    item = (item,) + ("",) * (self.nlevels - 1)
elif len(item) != self.nlevels:
    raise ValueError("Item must have length equal to number of levels.")
exit(item)
