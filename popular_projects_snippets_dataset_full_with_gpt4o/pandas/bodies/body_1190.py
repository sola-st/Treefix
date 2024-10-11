# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH 11278
ser = Series(range(20), index=idx)
df = DataFrame(range(20), index=idx)
msg = r"not in index"

with pytest.raises(KeyError, match=msg):
    ser.loc[labels]
with pytest.raises(KeyError, match=msg):
    ser[labels]
with pytest.raises(KeyError, match=msg):
    df.loc[labels]
