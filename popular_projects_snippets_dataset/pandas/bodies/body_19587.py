# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
    Merge blocks having same dtype, exclude non-consolidating blocks
    """
# sort by _can_consolidate, dtype
gkey = lambda x: x._consolidate_key
grouper = itertools.groupby(sorted(blocks, key=gkey), gkey)

new_blocks: list[Block] = []
for (_can_consolidate, dtype), group_blocks in grouper:
    merged_blocks, _ = _merge_blocks(
        list(group_blocks), dtype=dtype, can_consolidate=_can_consolidate
    )
    new_blocks = extend_blocks(merged_blocks, new_blocks)
exit(tuple(new_blocks))
