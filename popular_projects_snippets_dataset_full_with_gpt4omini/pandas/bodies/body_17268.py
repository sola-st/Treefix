# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

msg = 'For argument "inplace" expected type bool, received type'
with pytest.raises(ValueError, match=msg):
    df.copy().rename_axis(mapper={"a": "x", "b": "y"}, axis=1, inplace=value)

with pytest.raises(ValueError, match=msg):
    df.copy().drop("a", axis=1, inplace=value)

with pytest.raises(ValueError, match=msg):
    df.copy().fillna(value=0, inplace=value)

with pytest.raises(ValueError, match=msg):
    df.copy().replace(to_replace=1, value=7, inplace=value)

with pytest.raises(ValueError, match=msg):
    df.copy().interpolate(inplace=value)

with pytest.raises(ValueError, match=msg):
    df.copy()._where(cond=df.a > 2, inplace=value)

with pytest.raises(ValueError, match=msg):
    df.copy().mask(cond=df.a > 2, inplace=value)
