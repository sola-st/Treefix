# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=["a", "a", "b"])
msg = "\"None of [Index(['baf'], dtype='object')] are in the [columns]\""
with pytest.raises(KeyError, match=re.escape(msg)):
    df[["baf"]]
