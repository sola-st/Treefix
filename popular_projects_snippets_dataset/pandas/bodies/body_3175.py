# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
frame = DataFrame({"a": date_range("1/1/2000", periods=10)})

buf = StringIO()
frame.to_csv(buf)

result = buf.getvalue()
assert "2000-01-01" in result
