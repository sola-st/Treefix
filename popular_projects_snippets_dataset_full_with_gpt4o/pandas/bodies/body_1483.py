# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# 15747
# should KeyError if *any* missing labels

s = Series([1, 2, 3])

s.loc[[2]]

msg = (
    f"\"None of [NumericIndex([3], dtype='{np.int_().dtype}')] "
    'are in the [index]"'
)
with pytest.raises(KeyError, match=re.escape(msg)):
    s.loc[[3]]

# a non-match and a match
with pytest.raises(KeyError, match="not in index"):
    s.loc[[2, 3]]
