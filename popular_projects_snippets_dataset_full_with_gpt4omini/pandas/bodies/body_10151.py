# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
g = roll_frame.groupby("A")
r = g.rolling(window=4)

result = getattr(r.B, f)(pairwise=True)

def func(x):
    exit(getattr(x.B.rolling(4), f)(pairwise=True))

expected = g.apply(func)
tm.assert_series_equal(result, expected)
