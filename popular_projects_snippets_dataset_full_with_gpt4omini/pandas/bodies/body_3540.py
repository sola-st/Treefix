# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = frame_of_index_cols

msg = 'The parameter "keys" may be a column key, .*'
# forbidden type, e.g. set
with pytest.raises(TypeError, match=msg):
    df.set_index(box(df["A"]), drop=drop, append=append)

# forbidden type in list, e.g. set
with pytest.raises(TypeError, match=msg):
    df.set_index(["A", df["A"], box(df["A"])], drop=drop, append=append)
