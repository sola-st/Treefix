# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
df = datetime_frame
the_diff = df.diff(num)

expected = df["A"] - df["A"].shift(num)
tm.assert_series_equal(the_diff["A"], expected)
