# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 13354
margins_name = "Weekly"
costs = DataFrame(
    {
        "item": ["bacon", "cheese", "bacon", "cheese"],
        "cost": [2.5, 4.5, 3.2, 3.3],
        "day": ["M", "M", "T", "T"],
    }
)
table = costs.pivot_table(
    index="item",
    columns="day",
    margins=True,
    margins_name=margins_name,
    aggfunc=[np.mean, max],
)
ix = Index(["bacon", "cheese", margins_name], dtype="object", name="item")
tups = [
    ("mean", "cost", "M"),
    ("mean", "cost", "T"),
    ("mean", "cost", margins_name),
    ("max", "cost", "M"),
    ("max", "cost", "T"),
    ("max", "cost", margins_name),
]
cols = MultiIndex.from_tuples(tups, names=[None, None, "day"])
expected = DataFrame(table.values, index=ix, columns=cols)
tm.assert_frame_equal(table, expected)
