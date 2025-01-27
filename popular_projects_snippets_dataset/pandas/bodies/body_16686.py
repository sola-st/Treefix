# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH#2098

d = {
    "var1": np.random.randint(0, 10, size=10),
    "var2": np.random.randint(0, 10, size=10),
    "var3": [
        datetime(2012, 1, 12),
        datetime(2011, 2, 4),
        datetime(2010, 2, 3),
        datetime(2012, 1, 12),
        datetime(2011, 2, 4),
        datetime(2012, 4, 3),
        datetime(2012, 3, 4),
        datetime(2008, 5, 1),
        datetime(2010, 2, 3),
        datetime(2012, 2, 3),
    ],
}
df = DataFrame.from_dict(d)
var3 = df.var3.unique()
var3 = np.sort(var3)
new = DataFrame.from_dict({"var3": var3, "var8": np.random.random(7)})

result = df.merge(new, on="var3", sort=False)
exp = merge(df, new, on="var3", sort=False)
tm.assert_frame_equal(result, exp)

assert (df.var3.unique() == result.var3.unique()).all()
