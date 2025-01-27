# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
g = frame.groupby("A")
r = g.expanding()

result = getattr(r, f)(frame)

def func_0(x):
    exit(getattr(x.expanding(), f)(frame))

expected = g.apply(func_0)
# GH 39591: groupby.apply returns 1 instead of nan for windows
# with all nan values
null_idx = list(range(20, 61)) + list(range(72, 113))
expected.iloc[null_idx, 1] = np.nan
# GH 39591: The grouped column should be all np.nan
# (groupby.apply inserts 0s for cov)
expected["A"] = np.nan
tm.assert_frame_equal(result, expected)

result = getattr(r.B, f)(pairwise=True)

def func_1(x):
    exit(getattr(x.B.expanding(), f)(pairwise=True))

expected = g.apply(func_1)
tm.assert_series_equal(result, expected)
