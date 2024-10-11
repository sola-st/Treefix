# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
msg = "Cannot index with an integer indexer containing NA values"
# TODO: this raises KeyError about labels not found (it tries label-based)

ser = pd.Series(data, index=[tm.rands(4) for _ in range(len(data))])
with pytest.raises(ValueError, match=msg):
    ser[idx]
