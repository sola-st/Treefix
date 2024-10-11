# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 31016
df = DataFrame(
    {
        "A": ["foo", "foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar"],
        "B": ["one", "one", "one", "two", "two", "one", "one", "two", "two"],
        "C": [
            "small",
            "large",
            "large",
            "small",
            "small",
            "large",
            "small",
            "small",
            "large",
        ],
        "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
        "E": [2, 4, 5, 5, 6, 6, 8, 9, 9],
    }
)
if aggfunc != "sum":
    with pytest.raises(TypeError, match="Could not convert"):
        df.pivot_table(columns=columns, margins=True, aggfunc=aggfunc)
if "B" not in columns:
    df = df.drop(columns="B")
result = df.drop(columns="C").pivot_table(
    columns=columns, margins=True, aggfunc=aggfunc
)
expected = DataFrame(values, index=Index(["D", "E"]), columns=expected_columns)

tm.assert_frame_equal(result, expected)
