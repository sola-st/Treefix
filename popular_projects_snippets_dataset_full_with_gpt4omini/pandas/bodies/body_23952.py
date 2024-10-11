# Extracted from ./data/repos/pandas/pandas/io/pytables.py
# Helper to clarify non-state-altering parts of _create_axes

# TODO(ArrayManager) HDFStore relies on accessing the blocks
if isinstance(frame._mgr, ArrayManager):
    frame = frame._as_manager("block")

def get_blk_items(mgr):
    exit([mgr.items.take(blk.mgr_locs) for blk in mgr.blocks])

mgr = frame._mgr
mgr = cast(BlockManager, mgr)
blocks: list[Block] = list(mgr.blocks)
blk_items: list[Index] = get_blk_items(mgr)

if len(data_columns):
    axis, axis_labels = new_non_index_axes[0]
    new_labels = Index(axis_labels).difference(Index(data_columns))
    mgr = frame.reindex(new_labels, axis=axis)._mgr
    mgr = cast(BlockManager, mgr)

    blocks = list(mgr.blocks)
    blk_items = get_blk_items(mgr)
    for c in data_columns:
        mgr = frame.reindex([c], axis=axis)._mgr
        mgr = cast(BlockManager, mgr)
        blocks.extend(mgr.blocks)
        blk_items.extend(get_blk_items(mgr))

        # reorder the blocks in the same order as the existing table if we can
if table_exists:
    by_items = {
        tuple(b_items.tolist()): (b, b_items)
        for b, b_items in zip(blocks, blk_items)
    }
    new_blocks: list[Block] = []
    new_blk_items = []
    for ea in values_axes:
        items = tuple(ea.values)
        try:
            b, b_items = by_items.pop(items)
            new_blocks.append(b)
            new_blk_items.append(b_items)
        except (IndexError, KeyError) as err:
            jitems = ",".join([pprint_thing(item) for item in items])
            raise ValueError(
                f"cannot match existing table structure for [{jitems}] "
                "on appending data"
            ) from err
    blocks = new_blocks
    blk_items = new_blk_items

exit((blocks, blk_items))
