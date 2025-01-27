# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH4014 this used to raise ValueError since 'exp'>1 (in py2)
df = DataFrame({"exp": ["A"] * 3 + ["B"] * 3, "var1": range(6)}).set_index(
    "exp"
)
if axis in (1, "columns"):
    df = df.T
df.groupby(level="exp", axis=axis)
msg = f"level name foo is not the name of the {df._get_axis_name(axis)}"
with pytest.raises(ValueError, match=msg):
    df.groupby(level="foo", axis=axis)
