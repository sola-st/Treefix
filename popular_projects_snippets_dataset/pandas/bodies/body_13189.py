# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# test additional ExtensionArrays that are supported through the
# __arrow_array__ protocol
df = pd.DataFrame(
    {
        "a": pd.Series([1, 2, 3], dtype="Int64"),
        "b": pd.Series([1, 2, 3], dtype="UInt32"),
        "c": pd.Series(["a", None, "c"], dtype="string"),
    }
)
check_round_trip(df, pa)

df = pd.DataFrame({"a": pd.Series([1, 2, 3, None], dtype="Int64")})
check_round_trip(df, pa)
