# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
# GH#8569
idx = Index([1, 2], dtype=np.float64)
assert idx.get_loc(1) == 0
with pytest.raises(KeyError, match=r"^3$"):
    idx.get_loc(3)
with pytest.raises(KeyError, match="^nan$"):
    idx.get_loc(np.nan)
with pytest.raises(InvalidIndexError, match=r"\[nan\]"):
    # listlike/non-hashable raises TypeError
    idx.get_loc([np.nan])
