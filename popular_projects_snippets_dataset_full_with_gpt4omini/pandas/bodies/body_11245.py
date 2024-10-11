# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
msg = "Grouper for '<class 'pandas.core.frame.DataFrame'>' not 1-dimensional"
with pytest.raises(ValueError, match=msg):
    Grouping(df.index, df[["A", "A"]])
