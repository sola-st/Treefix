# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH 18321
s1 = Series(range(3), name=("a", "b"))
s2 = Series(range(3), name=("c", "d"))

expected = DataFrame(
    np.eye(3, dtype="int64"),
    index=Index(range(3), name=("a", "b")),
    columns=Index(range(3), name=("c", "d")),
)
result = crosstab(s1, s2)
tm.assert_frame_equal(result, expected)
