# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_cython.py
# ensure that the cython-based aggregations don't fail for nullable dtype
# (eg https://github.com/pandas-dev/pandas/issues/37415)
df = DataFrame(
    {
        "A": ["A", "B"] * 5,
        "B": pd.array([1, 2, 3, 4, 5, 6, 7, 8, 9, pd.NA], dtype="Int64"),
    }
)
result = getattr(df.groupby("A")["B"], op_name)()
df2 = df.assign(B=df["B"].astype("float64"))
expected = getattr(df2.groupby("A")["B"], op_name)()

if op_name != "count":
    # the result is not yet consistently using Int64/Float64 dtype,
    # so for now just checking the values by casting to float
    result = result.astype("float64")
tm.assert_series_equal(result, expected)
