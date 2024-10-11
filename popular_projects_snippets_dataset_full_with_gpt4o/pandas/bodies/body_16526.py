# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH 13279 / 22529

s1 = Series(range(3), name="foo")
s2_foo = Series(range(1, 4), name="foo")
s2_bar = Series(range(1, 4), name="bar")
s3 = Series(range(3), name="waldo")

# check result computed with duplicate labels against
# result computed with unique labels, then relabelled
mapper = {"bar": "foo"}

# duplicate row, column labels
result = crosstab(s1, s2_foo)
expected = crosstab(s1, s2_bar).rename_axis(columns=mapper, axis=1)
tm.assert_frame_equal(result, expected)

# duplicate row, unique column labels
result = crosstab([s1, s2_foo], s3)
expected = crosstab([s1, s2_bar], s3).rename_axis(index=mapper, axis=0)
tm.assert_frame_equal(result, expected)

# unique row, duplicate column labels
result = crosstab(s3, [s1, s2_foo])
expected = crosstab(s3, [s1, s2_bar]).rename_axis(columns=mapper, axis=1)

tm.assert_frame_equal(result, expected)
