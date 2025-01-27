# Extracted from ./data/repos/pandas/pandas/tests/strings/test_extract.py
s = Series(["a1a2", "b1", "c1"], name="xxx", dtype=any_string_dtype)
result = s.str.extractall(r"[ab](?P<digit>\d)")
expected = DataFrame(
    {"digit": ["1", "2", "1"]},
    index=MultiIndex.from_tuples([(0, 0), (0, 1), (1, 0)], names=[None, "match"]),
    dtype=any_string_dtype,
)
tm.assert_frame_equal(result, expected)

# index should return the same result as the default index without name thus
# index.name doesn't affect to the result
if any_string_dtype == "object":
    for idx in [
        Index(["a1a2", "b1", "c1"]),
        Index(["a1a2", "b1", "c1"], name="xxx"),
    ]:

        result = idx.str.extractall(r"[ab](?P<digit>\d)")
        tm.assert_frame_equal(result, expected)

s = Series(
    ["a1a2", "b1", "c1"],
    name="s_name",
    index=Index(["XX", "yy", "zz"], name="idx_name"),
    dtype=any_string_dtype,
)
result = s.str.extractall(r"[ab](?P<digit>\d)")
expected = DataFrame(
    {"digit": ["1", "2", "1"]},
    index=MultiIndex.from_tuples(
        [("XX", 0), ("XX", 1), ("yy", 0)], names=["idx_name", "match"]
    ),
    dtype=any_string_dtype,
)
tm.assert_frame_equal(result, expected)
