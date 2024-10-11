# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# see gh-1048
with pytest.raises(ValueError, match="No group keys passed!"):
    df.groupby([])
