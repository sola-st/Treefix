# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py

# joining dups
df = concat(
    [
        DataFrame(np.random.randn(10, 4), columns=["A", "A", "B", "B"]),
        DataFrame(
            np.random.randint(0, 10, size=20).reshape(10, 2), columns=["A", "C"]
        ),
    ],
    axis=1,
)

expected = concat([df, df], axis=1)
result = df.join(df, rsuffix="_2")
result.columns = expected.columns
tm.assert_frame_equal(result, expected)

# GH 4975, invalid join on dups
w = DataFrame(np.random.randn(4, 2), columns=["x", "y"])
x = DataFrame(np.random.randn(4, 2), columns=["x", "y"])
y = DataFrame(np.random.randn(4, 2), columns=["x", "y"])
z = DataFrame(np.random.randn(4, 2), columns=["x", "y"])

dta = x.merge(y, left_index=True, right_index=True).merge(
    z, left_index=True, right_index=True, how="outer"
)
# GH 40991: As of 2.0 causes duplicate columns
with pytest.raises(
    pd.errors.MergeError,
    match="Passing 'suffixes' which cause duplicate columns",
):
    dta.merge(w, left_index=True, right_index=True)
