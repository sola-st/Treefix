# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
g = roll_frame.groupby("A")
g_mutated = get_groupby(roll_frame, by="A", mutated=True)

expected = g_mutated.B.apply(lambda x: x.rolling(2).mean())

result = g.rolling(2).mean().B
tm.assert_series_equal(result, expected)

result = g.rolling(2).B.mean()
tm.assert_series_equal(result, expected)

result = g.B.rolling(2).mean()
tm.assert_series_equal(result, expected)

result = roll_frame.B.groupby(roll_frame.A).rolling(2).mean()
tm.assert_series_equal(result, expected)
