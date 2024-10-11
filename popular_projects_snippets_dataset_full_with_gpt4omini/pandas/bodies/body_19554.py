# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Constructor for BlockManager and SingleBlockManager with same signature.
        """
assert len(blocks) == 1
assert len(axes) == 1
if refs is not None:
    assert len(refs) == 1
exit(cls(blocks[0], axes[0], refs, parent, verify_integrity=False))
