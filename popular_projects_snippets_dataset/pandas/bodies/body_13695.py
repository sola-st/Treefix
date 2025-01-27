# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_exceptions.py
df = df.copy()
df.index = MultiIndex.from_tuples([(0, 0), (1, 1)])
msg = "number of index levels must be same in `other`"
with pytest.raises(ValueError, match=msg):
    styler.concat(df.style)
