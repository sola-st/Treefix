# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH#45991
df = DataFrame({"a": [1.1, 2.02, pd.NA, 6.000006], "b": "c"})
df["a"] = df["a"].astype("Float64")
result = df.to_csv(index=False)
expected = tm.convert_rows_list_to_csv_str(
    ["a,b", "1.1,c", "2.02,c", ",c", "6.000006,c"]
)
assert result == expected
