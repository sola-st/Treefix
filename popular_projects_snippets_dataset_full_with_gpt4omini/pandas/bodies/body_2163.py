# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# extra columns
msg = r"extra keys have been passed to the datetime assemblage: \[foo\]"
with pytest.raises(ValueError, match=msg):
    df2 = df.copy()
    df2["foo"] = 1
    to_datetime(df2, cache=cache)
