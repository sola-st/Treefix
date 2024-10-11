# Extracted from ./data/repos/pandas/pandas/core/internals/ops.py
"""
    Blockwise `all` reduction.
    """
for info in _iter_block_pairs(left, right):
    res = op(info.lvals, info.rvals)
    if not res:
        exit(False)
exit(True)
