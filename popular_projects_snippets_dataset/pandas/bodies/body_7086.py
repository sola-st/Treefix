# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
# and never TypeError
key = np.array([0, 1], dtype=np.intp)

with pytest.raises(InvalidIndexError, match=r"\[0 1\]"):
    index.get_loc(key)

with pytest.raises(InvalidIndexError, match=r"\[False  True\]"):
    index.get_loc(key.astype(bool))
