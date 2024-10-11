# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
df = DataFrame({"A": [1, 2, 3], "B": ["foo", "bar", "baz"]})

buf = StringIO()
df.to_csv(buf, index=False, quoting=csv.QUOTE_NONNUMERIC, encoding="utf-8")

result = buf.getvalue()
expected_rows = ['"A","B"', '1,"foo"', '2,"bar"', '3,"baz"']
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert result == expected
