# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_rank.py
df = DataFrame({"key": ["foo"] * 5, "val": vals})
msg = "na_option must be one of 'keep', 'top', or 'bottom'"

with pytest.raises(ValueError, match=msg):
    df.groupby("key").rank(
        method=ties_method, ascending=ascending, na_option=na_option, pct=pct
    )
