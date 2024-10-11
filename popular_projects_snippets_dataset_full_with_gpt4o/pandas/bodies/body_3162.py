# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, index=["one", "two", "three"])

buf = StringIO()
df.to_csv(buf, index_label=False)

expected_rows = ["A,B", "one,1,4", "two,2,5", "three,3,6"]
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert buf.getvalue() == expected
