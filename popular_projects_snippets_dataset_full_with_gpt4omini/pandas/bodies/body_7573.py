# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_missing.py
# GH 11343
msg = "isna is not defined for MultiIndex"
with pytest.raises(NotImplementedError, match=msg):
    idx.fillna(idx[0])
