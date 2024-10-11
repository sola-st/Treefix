# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# GH#47436
df = DataFrame({"a": [0.5, 1.0]})
result = df.to_csv(
    decimal=",",
    float_format=lambda x: np.format_float_positional(x, trim="-"),
    index=False,
)
expected_rows = ["a", "0.5", "1"]
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert result == expected
