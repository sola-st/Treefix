# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# GH#46297
df = DataFrame(
    {
        "a": [
            pd.Interval(
                Timestamp("2020-01-01"),
                Timestamp("2020-01-02"),
                closed="both",
            )
        ]
    }
)
df["a"] = df["a"].astype("category")
result = df.to_csv()
expected_rows = [",a", '0,"[2020-01-01, 2020-01-02]"']
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert result == expected
