# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_analytics.py

first = idx

# - now raises (previously was set op difference)
msg = "cannot perform __sub__ with this index type: MultiIndex"
with pytest.raises(TypeError, match=msg):
    first - idx[-3:]
with pytest.raises(TypeError, match=msg):
    idx[-3:] - first
with pytest.raises(TypeError, match=msg):
    idx[-3:] - first.tolist()
msg = "cannot perform __rsub__ with this index type: MultiIndex"
with pytest.raises(TypeError, match=msg):
    first.tolist() - idx[-3:]
