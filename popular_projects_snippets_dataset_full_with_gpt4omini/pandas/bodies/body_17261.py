# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py

# allow single item via bool method
df = DataFrame([[True]])
assert df.bool()

df = DataFrame([[False]])
assert not df.bool()

df = DataFrame([[False, False]])
msg = "The truth value of a DataFrame is ambiguous"
with pytest.raises(ValueError, match=msg):
    df.bool()
with pytest.raises(ValueError, match=msg):
    bool(df)
