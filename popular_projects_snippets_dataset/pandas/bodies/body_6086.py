# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
msg = "Cannot index with an integer indexer containing NA values"
with pytest.raises(ValueError, match=msg):
    data[idx]
