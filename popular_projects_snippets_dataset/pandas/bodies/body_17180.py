# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 9534
df = DataFrame(
    {"C1": ["A", "B", "C", "C"], "C2": ["a", "a", "b", "b"], "V": [1, 2, 3, 4]}
)
df["C1"] = df["C1"].astype("category")
result = df.pivot_table(
    "V", index="C1", columns="C2", dropna=observed, aggfunc="count"
)

expected_index = pd.CategoricalIndex(
    ["A", "B", "C"], categories=["A", "B", "C"], ordered=False, name="C1"
)
expected_columns = Index(["a", "b"], name="C2")
expected_data = np.array([[1, 0], [1, 0], [0, 2]], dtype=np.int64)
expected = DataFrame(
    expected_data, index=expected_index, columns=expected_columns
)
tm.assert_frame_equal(result, expected)
