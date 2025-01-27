# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_missing.py
# GH 14955
df = DataFrame({"a": [1, 2], "b": [1, 1]})
with pytest.raises(ValueError, match="Must specify a fill"):
    df.groupby("b").fillna()
