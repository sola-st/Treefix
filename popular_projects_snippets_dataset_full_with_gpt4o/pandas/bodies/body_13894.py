# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 29975
# Make sure full na_rep shows up when a dtype is provided
expected = tm.convert_rows_list_to_csv_str([",0", "0,a", "1,ZZZZZ", "2,c"])
csv = pd.Series(["a", pd.NA, "c"], dtype=nullable_string_dtype).to_csv(
    na_rep="ZZZZZ"
)
assert expected == csv
