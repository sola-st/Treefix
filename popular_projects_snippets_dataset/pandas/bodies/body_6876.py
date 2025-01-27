# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# don't test a MultiIndex here (as its tested separated)
index = index_flat

# GH 17896
expected = index.drop_duplicates()
for level in [0, index.name, None]:
    result = index.unique(level=level)
    tm.assert_index_equal(result, expected)

msg = "Too many levels: Index has only 1 level, not 4"
with pytest.raises(IndexError, match=msg):
    index.unique(level=3)

msg = (
    rf"Requested level \(wrong\) does not match index name "
    rf"\({re.escape(index.name.__repr__())}\)"
)
with pytest.raises(KeyError, match=msg):
    index.unique(level="wrong")
