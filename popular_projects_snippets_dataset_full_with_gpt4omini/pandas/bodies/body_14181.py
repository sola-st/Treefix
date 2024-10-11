# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
x = Series([Timestamp(200)])
result = fmt.Datetime64Formatter(x).get_result()
assert result[0].strip() == "1970-01-01 00:00:00.000000200"
