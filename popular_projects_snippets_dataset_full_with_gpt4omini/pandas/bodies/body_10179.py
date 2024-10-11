# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 32262
df = DataFrame([[1, 0]] * 20 + [[2, 0]] * 12 + [[3, 0]] * 8, columns=columns)
g = df.groupby("A")
original_obj = g.obj.copy(deep=True)
r = g.rolling(4)
result = r.sum()
assert "A" not in result.columns
tm.assert_frame_equal(g.obj, original_obj)
