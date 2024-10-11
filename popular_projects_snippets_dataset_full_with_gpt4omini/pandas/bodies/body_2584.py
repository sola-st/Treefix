# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#37672
df = DataFrame({"a": ["a"], "b": [1], "c": [1]})
if box == Series:
    indexer = box([], dtype="object")
else:
    indexer = box([])
msg = "Must have equal len keys and value when setting with an iterable"
with pytest.raises(ValueError, match=msg):
    df.loc[indexer, ["b"]] = [1]
