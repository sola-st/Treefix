# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
msg = "as_index=False only valid with DataFrame"
with pytest.raises(TypeError, match=msg):
    ts.groupby(lambda x: x.weekday(), as_index=False)

msg = "as_index=False only valid for axis=0"
with pytest.raises(ValueError, match=msg):
    df.groupby(lambda x: x.lower(), as_index=False, axis=1)
