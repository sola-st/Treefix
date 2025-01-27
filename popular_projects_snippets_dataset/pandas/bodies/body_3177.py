# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# GH#46812
df = DataFrame({"a": "x", "b": [1, pd.NA]})
df["b"] = df["b"].astype("Int16")
df["b"] = df["b"].astype("category")
result = df.to_csv()
expected_rows = [",a,b", "0,x,1", "1,x,"]
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert result == expected
