# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 25815
ordered_cat = pd.IntervalIndex.from_arrays([0, 0, 1, 1], [1, 1, 2, 2])
df = DataFrame(
    {
        "A": np.arange(4, 0, -1, dtype=np.intp),
        "B": ["a", "b", "a", "b"],
        "C": Categorical(ordered_cat, ordered=True).sort_values(
            ascending=False
        ),
    }
)

pivot_tab = pivot_table(
    df, index="C", columns="B", values="A", aggfunc="sum", margins=True
)

result = pivot_tab["All"]
expected = Series(
    [3, 7, 10],
    index=Index([pd.Interval(0, 1), pd.Interval(1, 2), "All"], name="C"),
    name="All",
    dtype=np.intp,
)
tm.assert_series_equal(result, expected)
