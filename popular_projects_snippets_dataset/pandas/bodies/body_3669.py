# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
# GH 29136
df = DataFrame([[1]])
msg = "Cannot specify both 'mapper' and any of 'index' or 'columns'"
with pytest.raises(TypeError, match=msg):
    df.rename({}, index={})

with pytest.raises(TypeError, match=msg):
    df.rename({}, columns={})

with pytest.raises(TypeError, match=msg):
    df.rename({}, columns={}, index={})
