# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 15631
x = DataFrame(zip(range(3), range(3)), columns=["a", "b"])

y = x.copy()
q = y.loc[:, "a"]
q += 2

tm.assert_frame_equal(x, y)

z = x.copy()
q = z.loc[x.index, "a"]
q += 2

tm.assert_frame_equal(x, z)
