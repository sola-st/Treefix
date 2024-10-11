# Extracted from ./data/repos/pandas/pandas/tests/extension/base/groupby.py
df = pd.DataFrame(
    {
        "A": [1, 1, 2, 2, 3, 3, 1, 4],
        "B": data_for_grouping,
        "C": [1, 1, 1, 1, 1, 1, 1, 1],
    }
)

dtype = data_for_grouping.dtype
if (
    is_numeric_dtype(dtype)
    or is_bool_dtype(dtype)
    or dtype.name == "decimal"
    or is_string_dtype(dtype)
    or is_period_dtype(dtype)
    or is_object_dtype(dtype)
):
    expected = pd.Index(["B", "C"])
    result = df.groupby("A").sum().columns
else:
    expected = pd.Index(["C"])
    with pytest.raises(TypeError, match="does not support"):
        df.groupby("A").sum().columns
    result = df.groupby("A").sum(numeric_only=True).columns
tm.assert_index_equal(result, expected)
