# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# GH4328
df = DataFrame({"A": ["hello", '{"hello"}']})
buf = StringIO()
df.to_csv(buf, quoting=csv.QUOTE_NONE, encoding=encoding, index=False)

result = buf.getvalue()
expected_rows = ["A", "hello", '{"hello"}']
expected = tm.convert_rows_list_to_csv_str(expected_rows)
assert result == expected
