# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# empty string
result = to_datetime("", cache=cache)
assert result is NaT
