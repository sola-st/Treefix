# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
if isinstance(index, MultiIndex):
    index = index.rename(["foo", "bar"] + index.names[2:])
    msg = f"'Level {label} not found'"
else:
    index = index.rename("foo")
    msg = rf"Requested level \({label}\) does not match index name \(foo\)"
with pytest.raises(KeyError, match=msg):
    index.isin([], level=label)
