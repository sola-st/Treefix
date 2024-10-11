# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = frame_of_index_cols

with pytest.raises(KeyError, match="['foo', 'bar', 'baz']"):
    # column names are A-E, as well as one tuple
    df.set_index(["foo", "bar", "baz"], drop=drop, append=append)

# non-existent key in list with arrays
with pytest.raises(KeyError, match="X"):
    df.set_index([df["A"], df["B"], "X"], drop=drop, append=append)

msg = "[('foo', 'foo', 'foo', 'bar', 'bar')]"
# tuples always raise KeyError
with pytest.raises(KeyError, match=msg):
    df.set_index(tuple(df["A"]), drop=drop, append=append)

# also within a list
with pytest.raises(KeyError, match=msg):
    df.set_index(["A", df["A"], tuple(df["A"])], drop=drop, append=append)
