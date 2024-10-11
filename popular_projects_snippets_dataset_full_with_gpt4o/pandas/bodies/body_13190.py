# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# test ArrowStringArray supported through the __arrow_array__ protocol
df = pd.DataFrame({"a": pd.Series(["a", None, "c"], dtype="string[pyarrow]")})
with pd.option_context("string_storage", string_storage):
    check_round_trip(df, pa, expected=df.astype(f"string[{string_storage}]"))
