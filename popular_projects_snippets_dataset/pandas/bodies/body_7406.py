# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_integrity.py
# should not segfault GH5123
# NOTE: if MI representation changes, may make sense to allow
# isna(MI)
msg = "isna is not defined for MultiIndex"
with pytest.raises(NotImplementedError, match=msg):
    pd.isna(idx)
