# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# see gh-25099
df = DataFrame({"c": [float("nan")] * 3})
df = df.astype(df_new_type)
expected_rows = ["c", "mynull", "mynull", "mynull"]
expected = tm.convert_rows_list_to_csv_str(expected_rows)

result = df.to_csv(index=False, na_rep="mynull", encoding="ascii")

assert expected == result
