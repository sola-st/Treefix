# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py

# GH 13174
g = roll_frame.groupby("A")
r = g.rolling(2, min_periods=0)
g_mutated = get_groupby(roll_frame, by="A", mutated=True)
expected = g_mutated.B.apply(lambda x: x.rolling(2, min_periods=0).count())

result = r.B.count()
tm.assert_series_equal(result, expected)

result = r.B.count()
tm.assert_series_equal(result, expected)
