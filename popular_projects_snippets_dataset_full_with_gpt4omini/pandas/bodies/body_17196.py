# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# The relevant characteristic is that the call
#  to maybe_downcast_to_dtype(agged[v], data[v].dtype) in
#  __internal_pivot_table has `agged[v]` a DataFrame instead of Series,
#  In this case this is because agged.columns is a MultiIndex and 'v'
#  is only indexing on its first level.
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

table = pivot_table(
    df,
    values=["D", "E"],
    index=["A", "C"],
    aggfunc={"D": np.mean, "E": [min, max, np.mean]},
)
cols = MultiIndex.from_tuples(
    [("D", "mean"), ("E", "max"), ("E", "mean"), ("E", "min")]
)
index = MultiIndex.from_tuples(
    [("bar", "large"), ("bar", "small"), ("foo", "large"), ("foo", "small")],
    names=["A", "C"],
)
vals = np.array(
    [
        [5.5, 9.0, 7.5, 6.0],
        [5.5, 9.0, 8.5, 8.0],
        [2.0, 5.0, 4.5, 4.0],
        [2.33333333, 6.0, 4.33333333, 2.0],
    ]
)
expected = DataFrame(vals, columns=cols, index=index)
expected[("E", "min")] = expected[("E", "min")].astype(np.int64)
expected[("E", "max")] = expected[("E", "max")].astype(np.int64)
tm.assert_frame_equal(table, expected)
