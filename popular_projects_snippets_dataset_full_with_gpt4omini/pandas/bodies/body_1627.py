# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#13831
vals = np.random.randn(8, 6)
idx = date_range("1/1/2000", periods=8)
cols = ["A", "B", "C", "D", "E", "F"]
exp = DataFrame(vals, index=idx, columns=cols)
exp.loc[exp.index[1], ("A", "B")] = np.nan
vals[1][0:2] = np.nan
res = DataFrame(vals, index=idx, columns=cols)
tm.assert_frame_equal(res, exp)
