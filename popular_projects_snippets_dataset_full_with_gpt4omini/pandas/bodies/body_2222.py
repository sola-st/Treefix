# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# Test that each of several string-accepting methods return pd.NaT
result1, _ = parsing.parse_datetime_string_with_reso("NaT")
result2 = to_datetime("NaT")
result3 = Timestamp("NaT")
result4 = DatetimeIndex(["NaT"])[0]
assert result1 is NaT
assert result2 is NaT
assert result3 is NaT
assert result4 is NaT
