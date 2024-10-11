# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
arr = np.array([parse("2012-06-13T01:39:00Z")], dtype=object)

result = to_datetime(arr, utc=True)
assert result.tz is timezone.utc
