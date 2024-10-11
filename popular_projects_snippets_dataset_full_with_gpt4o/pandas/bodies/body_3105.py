# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#9416
s1 = Series(["a", "b", "c"], dtype="category")
s2 = Series(["A", "B", "C"], dtype="category")
df = DataFrame({"one": s1, "two": s2})
rs = df.shift(1)
xp = DataFrame({"one": s1.shift(1), "two": s2.shift(1)})
tm.assert_frame_equal(rs, xp)
