# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_quantile.py
# GH#37493
df = DataFrame(
    {"a": [1, 1, 1, 2], "b": [1, 2, 3, pd.NA]}, dtype=any_numeric_ea_dtype
)
result = df.groupby("a").quantile(q=[0.5, 0.75], interpolation=interpolation)

if any_numeric_ea_dtype == "Float32":
    expected_dtype = any_numeric_ea_dtype
else:
    expected_dtype = "Float64"

expected = DataFrame(
    {"b": [2.0, 2.5, pd.NA, pd.NA]},
    dtype=expected_dtype,
    index=pd.MultiIndex.from_arrays(
        [
            pd.Series([1, 1, 2, 2], dtype=any_numeric_ea_dtype),
            [0.5, 0.75, 0.5, 0.75],
        ],
        names=["a", None],
    ),
)
tm.assert_frame_equal(result, expected)
