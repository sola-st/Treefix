# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unstack.py

mi = tm.makeTimeDataFrame().stack().index.rename(["major", "minor"])
ser = Series(["foo"] * len(mi), index=mi, name="category", dtype="category")

result = ser.unstack()

dti = ser.index.levels[0]
c = pd.Categorical(["foo"] * len(dti))
expected = DataFrame(
    {"A": c.copy(), "B": c.copy(), "C": c.copy(), "D": c.copy()},
    columns=pd.Index(list("ABCD"), name="minor"),
    index=dti.rename("major"),
)
tm.assert_frame_equal(result, expected)
