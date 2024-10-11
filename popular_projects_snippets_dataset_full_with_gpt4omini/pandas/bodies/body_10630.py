# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH25719, test for DataFrameGroupby.agg with multiple lambdas
# with mixed aggfunc
df = DataFrame(
    {
        "kind": ["cat", "dog", "cat", "dog"],
        "height": [9.1, 6.0, 9.5, 34.0],
        "weight": [7.9, 7.5, 9.9, 198.0],
    }
)
columns = [
    "height_sqr_min",
    "height_max",
    "weight_max",
    "height_max_2",
    "weight_min",
]
expected = DataFrame(
    {
        "height_sqr_min": [82.81, 36.00],
        "height_max": [9.5, 34.0],
        "weight_max": [9.9, 198.0],
        "height_max_2": [9.5, 34.0],
        "weight_min": [7.9, 7.5],
    },
    index=Index(["cat", "dog"], name="kind"),
    columns=columns,
)

# check agg(key=(col, aggfunc)) case
result1 = df.groupby(by="kind").agg(
    height_sqr_min=("height", lambda x: np.min(x**2)),
    height_max=("height", "max"),
    weight_max=("weight", "max"),
    height_max_2=("height", lambda x: np.max(x)),
    weight_min=("weight", lambda x: np.min(x)),
)
tm.assert_frame_equal(result1, expected)

# check pd.NamedAgg case
result2 = df.groupby(by="kind").agg(
    height_sqr_min=pd.NamedAgg(
        column="height", aggfunc=lambda x: np.min(x**2)
    ),
    height_max=pd.NamedAgg(column="height", aggfunc="max"),
    weight_max=pd.NamedAgg(column="weight", aggfunc="max"),
    height_max_2=pd.NamedAgg(column="height", aggfunc=lambda x: np.max(x)),
    weight_min=pd.NamedAgg(column="weight", aggfunc=lambda x: np.min(x)),
)
tm.assert_frame_equal(result2, expected)
