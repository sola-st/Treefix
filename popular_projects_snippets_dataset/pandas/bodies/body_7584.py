# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
df = tm.makeTimeDataFrame()
stacked = df.stack()
idx = stacked.index
with pytest.raises(TypeError, match="^Level type mismatch"):
    idx.slice_locs((1, 3))
with pytest.raises(TypeError, match="^Level type mismatch"):
    idx.slice_locs(df.index[5] + timedelta(seconds=30), (5, 2))
df = tm.makeCustomDataframe(5, 5)
stacked = df.stack()
idx = stacked.index
with pytest.raises(TypeError, match="^Level type mismatch"):
    idx.slice_locs(timedelta(seconds=30))
# TODO: Try creating a UnicodeDecodeError in exception message
with pytest.raises(TypeError, match="^Level type mismatch"):
    idx.slice_locs(df.index[1], (16, "a"))
