# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
# GH29522
s = Series(
    range(6),
    MultiIndex.from_product([["A", "B"], [1, 2, 3]], names=["lev1", "lev2"]),
    name="Amount",
)
df = DataFrame({"lev1": list("AAABBB"), "lev2": [1, 2, 3, 1, 2, 3], "col": 0})
result = merge(df, s.reset_index(), on=["lev1", "lev2"])
expected = DataFrame(
    {
        "lev1": list("AAABBB"),
        "lev2": [1, 2, 3, 1, 2, 3],
        "col": [0] * 6,
        "Amount": range(6),
    }
)
tm.assert_frame_equal(result, expected)
