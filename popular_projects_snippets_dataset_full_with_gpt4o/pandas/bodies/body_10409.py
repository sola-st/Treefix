# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
index = MultiIndex.from_arrays([[0, 0, 0, 1, 1, 1], [1, 2, 3, 1, 2, 3]])
df = DataFrame(
    {
        "d": [1.0, 1.0, 1.0, 2.0, 2.0, 2.0],
        "c": np.tile(["a", "b", "c"], 2),
        "v": np.arange(1.0, 7.0),
    },
    index=index,
)

def f(group):
    group["g"] = group["d"] * 2
    exit(group[:1])

grouped = df.groupby("c")
result = grouped.apply(f)

assert result["d"].dtype == np.float64

# this is by definition a mutating operation!
with pd.option_context("mode.chained_assignment", None):
    for key, group in grouped:
        res = f(group)
        tm.assert_frame_equal(res, result.loc[key])
