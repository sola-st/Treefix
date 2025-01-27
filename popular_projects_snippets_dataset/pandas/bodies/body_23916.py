# Extracted from ./data/repos/pandas/pandas/io/pytables.py
super().write(obj, **kwargs)

# TODO(ArrayManager) HDFStore relies on accessing the blocks
if isinstance(obj._mgr, ArrayManager):
    obj = obj._as_manager("block")

data = obj._mgr
if not data.is_consolidated():
    data = data.consolidate()

self.attrs.ndim = data.ndim
for i, ax in enumerate(data.axes):
    if i == 0 and (not ax.is_unique):
        raise ValueError("Columns index has to be unique for fixed format")
    self.write_index(f"axis{i}", ax)

# Supporting mixed-type DataFrame objects...nontrivial
self.attrs.nblocks = len(data.blocks)
for i, blk in enumerate(data.blocks):
    # I have no idea why, but writing values before items fixed #2299
    blk_items = data.items.take(blk.mgr_locs)
    self.write_array(f"block{i}_values", blk.values, items=blk_items)
    self.write_index(f"block{i}_items", blk_items)
