# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_join.py
# some corner cases
index = Index(["three", "one", "two"])
result = index.join(idx, level="second")
assert isinstance(result, MultiIndex)

with pytest.raises(TypeError, match="Join.*MultiIndex.*ambiguous"):
    idx.join(idx, level=1)
