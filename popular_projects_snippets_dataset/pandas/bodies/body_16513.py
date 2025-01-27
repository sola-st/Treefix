# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GS 10291

s1 = Series([1, 2, 3], index=[1, 2, 3])
s2 = Series([4, 5, 6], index=[4, 5, 6])

actual = crosstab(s1, s2)
expected = DataFrame(
    index=Index([], dtype="int64", name="row_0"),
    columns=Index([], dtype="int64", name="col_0"),
)

tm.assert_frame_equal(actual, expected)
