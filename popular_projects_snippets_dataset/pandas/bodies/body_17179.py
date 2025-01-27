# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# gh-21370
idx = [np.nan, "low", "high", "low", np.nan]
col = [np.nan, "A", "B", np.nan, "A"]
df = DataFrame(
    {
        "In": Categorical(idx, categories=["low", "high"], ordered=ordered),
        "Col": Categorical(col, categories=["A", "B"], ordered=ordered),
        "Val": range(1, 6),
    }
)
# case with index/columns/value
result = df.pivot_table(
    index="In", columns="Col", values="Val", observed=observed
)

expected_cols = pd.CategoricalIndex(["A", "B"], ordered=ordered, name="Col")

expected = DataFrame(data=[[2.0, np.nan], [np.nan, 3.0]], columns=expected_cols)
expected.index = Index(
    Categorical(["low", "high"], categories=["low", "high"], ordered=ordered),
    name="In",
)

tm.assert_frame_equal(result, expected)

# case with columns/value
result = df.pivot_table(columns="Col", values="Val", observed=observed)

expected = DataFrame(
    data=[[3.5, 3.0]], columns=expected_cols, index=Index(["Val"])
)

tm.assert_frame_equal(result, expected)
