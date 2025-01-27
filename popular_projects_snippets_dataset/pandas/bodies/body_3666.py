# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
# see gh-12392
df = DataFrame({"A": [1, 2], "B": [1, 2]}, index=["0", "1"])

# Named target and axis
over_spec_msg = "Cannot specify both 'axis' and any of 'index' or 'columns'"
with pytest.raises(TypeError, match=over_spec_msg):
    df.rename(index=str.lower, axis=1)

with pytest.raises(TypeError, match=over_spec_msg):
    df.rename(index=str.lower, axis="columns")

with pytest.raises(TypeError, match=over_spec_msg):
    df.rename(columns=str.lower, axis="columns")

with pytest.raises(TypeError, match=over_spec_msg):
    df.rename(index=str.lower, axis=0)

# Multiple targets and axis
with pytest.raises(TypeError, match=over_spec_msg):
    df.rename(str.lower, index=str.lower, axis="columns")

# Too many targets
over_spec_msg = "Cannot specify both 'mapper' and any of 'index' or 'columns'"
with pytest.raises(TypeError, match=over_spec_msg):
    df.rename(str.lower, index=str.lower, columns=str.lower)

# Duplicates
with pytest.raises(TypeError, match="multiple values"):
    df.rename(id, mapper=id)
