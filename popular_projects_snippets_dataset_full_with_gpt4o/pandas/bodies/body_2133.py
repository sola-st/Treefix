# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 24415
result = to_datetime(ts, utc=True)
assert result == expected
