# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
    Merge blocks having same dtype, exclude non-consolidating blocks, handling
    refs
    """
gkey = lambda x: x[0]._consolidate_key
grouper = itertools.groupby(sorted(zip(blocks, refs), key=gkey), gkey)

new_blocks: list[Block] = []
new_refs: list[weakref.ref | None] = []
for (_can_consolidate, dtype), group_blocks_refs in grouper:
    group_blocks, group_refs = list(zip(*list(group_blocks_refs)))
    merged_blocks, consolidated = _merge_blocks(
        list(group_blocks), dtype=dtype, can_consolidate=_can_consolidate
    )
    new_blocks = extend_blocks(merged_blocks, new_blocks)
    if consolidated:
        new_refs.extend([None])
    else:
        new_refs.extend(group_refs)
exit((tuple(new_blocks), new_refs))
