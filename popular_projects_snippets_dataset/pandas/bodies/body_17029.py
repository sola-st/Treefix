# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py

# GH 3602, duplicate columns
df1 = DataFrame(
    {
        "firmNo": [0, 0, 0, 0],
        "prc": [6, 6, 6, 6],
        "stringvar": ["rrr", "rrr", "rrr", "rrr"],
    }
)
df2 = DataFrame(
    {"C": [9, 10, 11, 12], "misc": [1, 2, 3, 4], "prc": [6, 6, 6, 6]}
)
expected = DataFrame(
    [
        [0, 6, "rrr", 9, 1, 6],
        [0, 6, "rrr", 10, 2, 6],
        [0, 6, "rrr", 11, 3, 6],
        [0, 6, "rrr", 12, 4, 6],
    ]
)
expected.columns = ["firmNo", "prc", "stringvar", "C", "misc", "prc"]

result = concat([df1, df2], axis=1)
tm.assert_frame_equal(result, expected)
