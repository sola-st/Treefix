# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

df = regular

# not a valid column
msg = (
    r"invalid on specified as foobar, must be a column "
    "\\(of DataFrame\\), an Index or None"
)
with pytest.raises(ValueError, match=msg):
    df.rolling(window="2s", on="foobar")

# column is valid
df = df.copy()
df["C"] = date_range("20130101", periods=len(df))
df.rolling(window="2d", on="C").sum()

# invalid columns
msg = "window must be an integer"
with pytest.raises(ValueError, match=msg):
    df.rolling(window="2d", on="B")

# ok even though on non-selected
df.rolling(window="2d", on="C").B.sum()
