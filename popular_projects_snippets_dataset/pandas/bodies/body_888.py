# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
blk = obj._mgr.blocks[0]
if inplace:
    assert blk._can_hold_element(elem)
else:
    assert not blk._can_hold_element(elem)
