# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH 19086 : int is casted to bool, but not vice-versa (for object dtype)
#  With bool dtype, we don't cast in either direction.
levels = [Index([False, True], dtype=dtype), np.arange(2, dtype="int64")]
idx = MultiIndex.from_product(levels)

if dtype is bool:
    with pytest.raises(KeyError, match=r"^\(0, 1\)$"):
        assert idx.get_loc((0, 1)) == 1
    with pytest.raises(KeyError, match=r"^\(1, 0\)$"):
        assert idx.get_loc((1, 0)) == 2
else:
    # We use python object comparisons, which treat 0 == False and 1 == True
    assert idx.get_loc((0, 1)) == 1
    assert idx.get_loc((1, 0)) == 2

with pytest.raises(KeyError, match=r"^\(False, True\)$"):
    idx.get_loc((False, True))
with pytest.raises(KeyError, match=r"^\(True, False\)$"):
    idx.get_loc((True, False))
