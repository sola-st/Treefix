# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 16037
df = DataFrame({"A": ["a"] * 4, "B": range(4)})
result = getattr(df.groupby("A").ewm(com=1.0), method)()
expected = DataFrame(
    {"B": expected_data},
    index=MultiIndex.from_tuples(
        [
            ("a", 0, "B"),
            ("a", 1, "B"),
            ("a", 2, "B"),
            ("a", 3, "B"),
        ],
        names=["A", None, None],
    ),
)
tm.assert_frame_equal(result, expected)

expected = df.groupby("A").apply(lambda x: getattr(x.ewm(com=1.0), method)())
tm.assert_frame_equal(result, expected)
