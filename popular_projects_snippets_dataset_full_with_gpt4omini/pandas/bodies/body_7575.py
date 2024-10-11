# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_missing.py
# this is really a smoke test for the methods
# as these are adequately tested for function elsewhere

msg = "isna is not defined for MultiIndex"
with pytest.raises(NotImplementedError, match=msg):
    idx.isna()
