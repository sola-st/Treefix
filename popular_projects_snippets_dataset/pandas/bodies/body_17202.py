# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH#48683
df = DataFrame(
    {
        "a": "A",
        "b": [1, 2],
        "date": pd.Timestamp("2019-12-31"),
        "sales": [10.0, 11],
    }
)
with tm.assert_produces_warning(None):
    result = df.pivot_table(
        index=["b", "date"], columns="a", margins=True, aggfunc="sum"
    )
expected = DataFrame(
    [[10.0, 10.0], [11.0, 11.0], [21.0, 21.0]],
    index=MultiIndex.from_arrays(
        [
            Index([1, 2, "All"], name="b"),
            Index(
                [pd.Timestamp("2019-12-31"), pd.Timestamp("2019-12-31"), ""],
                dtype=object,
                name="date",
            ),
        ]
    ),
    columns=MultiIndex.from_tuples(
        [("sales", "A"), ("sales", "All")], names=[None, "a"]
    ),
)
tm.assert_frame_equal(result, expected)
