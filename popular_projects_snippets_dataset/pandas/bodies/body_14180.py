# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
x = Series([datetime(2013, 1, 1), datetime(2013, 1, 2), NaT])
result = fmt.Datetime64Formatter(x).get_result()
assert result[0].strip() == "2013-01-01"
assert result[1].strip() == "2013-01-02"
