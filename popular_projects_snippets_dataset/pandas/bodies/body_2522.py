# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH 13522
df = DataFrame(index=["A", "B", "C"])
df["X"] = df.index
df["X"] = ["x", "y", "z"]
exp = DataFrame(data={"X": ["x", "y", "z"]}, index=["A", "B", "C"])
tm.assert_frame_equal(df, exp)
