# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH#32646 raise NotImplementedError instead of less-informative error
mi = MultiIndex.from_product([["a", "b"], [1, 2]])

idx = mi.levels[1]

msg = "Can only union MultiIndex with MultiIndex or Index of tuples"
with pytest.raises(NotImplementedError, match=msg):
    mi.union(idx)
