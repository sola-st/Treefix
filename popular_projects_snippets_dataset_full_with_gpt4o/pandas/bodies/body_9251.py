# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
# GH#21508
cat = Categorical(list("aabbca"), categories=list("cab"))

assert "b" in cat
assert "z" not in cat
assert np.nan not in cat
with pytest.raises(TypeError, match="unhashable type: 'list'"):
    assert [1] in cat

# assert codes NOT in index
assert 0 not in cat
assert 1 not in cat

cat = Categorical(list("aabbca") + [np.nan], categories=list("cab"))
assert np.nan in cat
