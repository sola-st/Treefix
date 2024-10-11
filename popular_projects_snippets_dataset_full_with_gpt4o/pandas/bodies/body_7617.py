# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# raise KeyError, not TypeError
mi = MultiIndex.from_product([range(3), range(4), range(5), range(6)])
key = ((2, 3, 4), "foo")

with pytest.raises(KeyError, match=re.escape(str(key))):
    mi.get_loc(key)
