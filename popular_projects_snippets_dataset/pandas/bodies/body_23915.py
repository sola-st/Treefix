# Extracted from ./data/repos/pandas/pandas/io/pytables.py
# start, stop applied to rows, so 0th axis only
self.validate_read(columns, where)
select_axis = self.obj_type()._get_block_manager_axis(0)

axes = []
for i in range(self.ndim):

    _start, _stop = (start, stop) if i == select_axis else (None, None)
    ax = self.read_index(f"axis{i}", start=_start, stop=_stop)
    axes.append(ax)

items = axes[0]
dfs = []

for i in range(self.nblocks):

    blk_items = self.read_index(f"block{i}_items")
    values = self.read_array(f"block{i}_values", start=_start, stop=_stop)

    columns = items[items.get_indexer(blk_items)]
    df = DataFrame(values.T, columns=columns, index=axes[1])
    dfs.append(df)

if len(dfs) > 0:
    out = concat(dfs, axis=1, copy=True)
    out = out.reindex(columns=items, copy=False)
    exit(out)

exit(DataFrame(columns=axes[0], index=axes[1]))
