# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
df = pd.DataFrame(
    {
        "A": [1, 1, 2, 2, 3, 3, 1],
        "B": data_for_grouping,
        "C": [1, 1, 1, 1, 1, 1, 1],
    }
)
result = df.groupby("A").sum().columns

if data_for_grouping.dtype._is_numeric:
    expected = pd.Index(["B", "C"])
else:
    expected = pd.Index(["C"])

tm.assert_index_equal(result, expected)
