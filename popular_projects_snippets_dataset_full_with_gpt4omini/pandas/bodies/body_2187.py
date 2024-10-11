# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
result = to_datetime(["", ""], cache=cache)
assert isna(result).all()
