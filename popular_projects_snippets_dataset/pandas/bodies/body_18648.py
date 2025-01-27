# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
# GH#30419 fix typing in StringHashTable.set_item to prevent segfault
tbl = ht.StringHashTable()

tbl.set_item("key", 1)
assert tbl.get_item("key") == 1

with pytest.raises(TypeError, match="'key' has incorrect type"):
    # key arg typed as string, not object
    tbl.set_item(4, 6)
with pytest.raises(TypeError, match="'val' has incorrect type"):
    tbl.get_item(4)
