# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
result = to_timedelta(["", ""])
assert isna(result).all()
