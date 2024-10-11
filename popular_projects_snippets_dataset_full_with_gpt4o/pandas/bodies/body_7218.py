# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
idx = Index([0.0, 1.0, 2.0], dtype=np.float64)

with pytest.raises(KeyError, match="^'foo'$"):
    idx.get_loc("foo")
with pytest.raises(KeyError, match=r"^1\.5$"):
    idx.get_loc(1.5)
with pytest.raises(KeyError, match="^True$"):
    idx.get_loc(True)
with pytest.raises(KeyError, match="^False$"):
    idx.get_loc(False)
