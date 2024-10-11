# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH 8569
idx = MultiIndex.from_arrays([[1.0, 2.0], [3.0, 4.0]])
assert isinstance(idx.get_loc(1), slice)
with pytest.raises(KeyError, match=r"^3$"):
    idx.get_loc(3)
with pytest.raises(KeyError, match=r"^nan$"):
    idx.get_loc(np.nan)
with pytest.raises(InvalidIndexError, match=r"\[nan\]"):
    # listlike/non-hashable raises TypeError
    idx.get_loc([np.nan])
