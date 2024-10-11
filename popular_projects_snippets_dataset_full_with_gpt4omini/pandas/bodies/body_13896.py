# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH#21734
df = DataFrame(
    {
        "date": pd.to_datetime("1970-01-01"),
        "datetime": pd.date_range("1970-01-01", periods=2, freq="H"),
    }
)
expected_rows = [
    "date,datetime",
    "1970-01-01,1970-01-01 00:00:00",
    "1970-01-01,1970-01-01 01:00:00",
]
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert df.to_csv(index=False) == expected
