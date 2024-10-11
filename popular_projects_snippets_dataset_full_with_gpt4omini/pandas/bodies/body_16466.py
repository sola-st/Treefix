# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
expected = DataFrame(
    {
        ("A", "a"): df1[("A", "a")],
        "CAP": ["B"] * len(df1),
        "low": ["b"] * len(df1),
        "value": df1[("B", "b")],
    },
    columns=[("A", "a"), "CAP", "low", "value"],
)

result = df1.melt(id_vars=[("A", "a")], value_vars=[("B", "b")])
tm.assert_frame_equal(result, expected)
