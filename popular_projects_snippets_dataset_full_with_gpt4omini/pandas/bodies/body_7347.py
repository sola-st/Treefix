# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
obj = frame_or_series(range(10), index=tdi)

msg = (
    "cannot do slice indexing on TimedeltaIndex with these "
    r"indexers \[foo\] of type str"
)
with pytest.raises(TypeError, match=msg):
    indexer_sl(obj)["foo":]
with pytest.raises(TypeError, match=msg):
    indexer_sl(obj)["foo":-1]
with pytest.raises(TypeError, match=msg):
    indexer_sl(obj)[:"foo"]
with pytest.raises(TypeError, match=msg):
    indexer_sl(obj)[tdi[0] : "foo"]
