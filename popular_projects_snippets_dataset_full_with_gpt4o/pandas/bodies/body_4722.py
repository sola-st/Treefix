# Extracted from ./data/repos/pandas/pandas/tests/strings/test_extract.py
# Contains tests like those in test_match and some others.
s = Series(["fooBAD__barBAD", np.nan, "foo"], dtype=any_string_dtype)

result = s.str.extract(".*(BAD[_]+).*(BAD)", expand=True)
expected = DataFrame(
    [["BAD__", "BAD"], [np.nan, np.nan], [np.nan, np.nan]], dtype=any_string_dtype
)
tm.assert_frame_equal(result, expected)
