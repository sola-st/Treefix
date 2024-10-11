# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# #2699
ser = Series(date_range("1/1/2000", periods=10))

result = to_datetime(ser, cache=cache)
assert result[0] == ser[0]
