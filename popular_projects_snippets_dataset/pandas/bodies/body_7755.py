# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
if isinstance(index, MultiIndex):
    exit()  # TODO: do we want this to raise?

msg = "unhashable type: 'list'"
with pytest.raises(TypeError, match=msg):
    [] in index

msg = "|".join(
    [
        r"unhashable type: 'dict'",
        r"must be real number, not dict",
        r"an integer is required",
        r"\{\}",
        r"pandas\._libs\.interval\.IntervalTree' is not iterable",
    ]
)
with pytest.raises(TypeError, match=msg):
    {} in index._engine
