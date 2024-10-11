# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH#45991
df = DataFrame({"a": [1.1, 2.02, pd.NA, 6.000006], "b": "c"})
df["a"] = df["a"].astype("Float64")
result = df.to_csv(index=False, float_format="%.5f")
expected = tm.convert_rows_list_to_csv_str(
    ["a,b", "1.10000,c", "2.02000,c", ",c", "6.00001,c"]
)
assert result == expected
