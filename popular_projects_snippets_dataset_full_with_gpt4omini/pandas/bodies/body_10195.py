# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 16037
df = DataFrame({"A": ["a"] * 4, "B": range(4)})
result = getattr(df.groupby("A").ewm(com=1.0), method)()
expected = DataFrame(
    {"B": expected_data},
    index=MultiIndex.from_tuples(
        [
            ("a", 0),
            ("a", 1),
            ("a", 2),
            ("a", 3),
        ],
        names=["A", None],
    ),
)
tm.assert_frame_equal(result, expected)
