# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reindex.py
# GH7774
idx = MultiIndex.from_product([[0, 1], ["a", "b"]], names=["foo", "bar"])
assert idx.reindex([], level=0)[0].names == ["foo", "bar"]
assert idx.reindex([], level=1)[0].names == ["foo", "bar"]
