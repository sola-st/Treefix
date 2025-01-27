# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
g = roll_frame.groupby("A")
r = g.rolling(window=4)

result = getattr(r, f)(roll_frame)

def func(x):
    exit(getattr(x.rolling(4), f)(roll_frame))

expected = g.apply(func)
# GH 39591: The grouped column should be all np.nan
# (groupby.apply inserts 0s for cov)
expected["A"] = np.nan
tm.assert_frame_equal(result, expected)
