# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# #2199
df = DataFrame({"a": [1, 2, 3]})
message = f"{bool_value}: boolean label can not be used without a boolean index"
with pytest.raises(KeyError, match=message):
    df.loc[bool_value]

msg = "cannot use a single bool to index into setitem"
with pytest.raises(KeyError, match=msg):
    df.loc[bool_value] = 0
