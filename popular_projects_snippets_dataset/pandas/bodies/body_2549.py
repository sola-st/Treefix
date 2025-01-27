# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#7655, test that assigning to a sub-frame of a frame
# with multi-index columns aligns both rows and columns
it = ["jim", "joe", "jolie"], ["first", "last"], ["left", "center", "right"]

cols = MultiIndex.from_product(it)
index = date_range("20141006", periods=20)
vals = np.random.randint(1, 1000, (len(index), len(cols)))
df = DataFrame(vals, columns=cols, index=index)

i, j = df.index.values.copy(), it[-1][:]

np.random.shuffle(i)
df["jim"] = df["jolie"].loc[i, ::-1]
tm.assert_frame_equal(df["jim"], df["jolie"])

np.random.shuffle(j)
df[("joe", "first")] = df[("jolie", "last")].loc[i, j]
tm.assert_frame_equal(df[("joe", "first")], df[("jolie", "last")])

np.random.shuffle(j)
df[("joe", "last")] = df[("jolie", "first")].loc[i, j]
tm.assert_frame_equal(df[("joe", "last")], df[("jolie", "first")])
