# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
locs = []
lengths = []

# 0-length OK
BlockIndex(0, locs, lengths)

# also OK even though empty
BlockIndex(1, locs, lengths)

msg = "Block 0 extends beyond end"
with pytest.raises(ValueError, match=msg):
    BlockIndex(10, [5], [10])

msg = "Block 0 overlaps"
with pytest.raises(ValueError, match=msg):
    BlockIndex(10, [2, 5], [5, 3])
