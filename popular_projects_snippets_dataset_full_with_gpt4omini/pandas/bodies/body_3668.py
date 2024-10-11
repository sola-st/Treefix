# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
# GH 29136
df = DataFrame([[1]])
msg = "must pass an index to rename"
with pytest.raises(TypeError, match=msg):
    df.rename()

with pytest.raises(TypeError, match=msg):
    df.rename(None, index=None)

with pytest.raises(TypeError, match=msg):
    df.rename(None, columns=None)

with pytest.raises(TypeError, match=msg):
    df.rename(None, columns=None, index=None)
