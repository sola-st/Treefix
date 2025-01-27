# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 26583
result = to_datetime(int_date, format="%Y%m%d", errors="ignore")
assert result == expected
