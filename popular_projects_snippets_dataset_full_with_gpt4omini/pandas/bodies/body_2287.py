# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_delitem.py
midx = MultiIndex.from_product([["A", "B"], [1, 2]])
df = DataFrame(np.random.randn(4, 4), columns=midx)
assert len(df.columns) == 4
assert ("A",) in df.columns
assert "A" in df.columns

result = df["A"]
assert isinstance(result, DataFrame)
del df["A"]

assert len(df.columns) == 2

# A still in the levels, BUT get a KeyError if trying
# to delete
assert ("A",) not in df.columns
with pytest.raises(KeyError, match=re.escape("('A',)")):
    del df[("A",)]

# behavior of dropped/deleted MultiIndex levels changed from
# GH 2770 to GH 19027: MultiIndex no longer '.__contains__'
# levels which are dropped/deleted
assert "A" not in df.columns
with pytest.raises(KeyError, match=re.escape("('A',)")):
    del df["A"]
