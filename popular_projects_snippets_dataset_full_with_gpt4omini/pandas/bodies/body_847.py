# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
"""compare the blocks, numeric compare ==, object don't"""
old_blocks = set(old_mgr.blocks)
new_blocks = set(new_mgr.blocks)
assert len(old_blocks) == len(new_blocks)

# compare non-numeric
for b in old_blocks:
    found = False
    for nb in new_blocks:
        if (b.values == nb.values).all():
            found = True
            break
    assert found

for b in new_blocks:
    found = False
    for ob in old_blocks:
        if (b.values == ob.values).all():
            found = True
            break
    assert found
