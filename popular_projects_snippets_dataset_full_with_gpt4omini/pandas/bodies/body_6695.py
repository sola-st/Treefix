# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_range.py
# index truncates early if freq causes end to be skipped
result = interval_range(start=start, end=end, freq=freq)
result_endpoint = result.right[-1]
assert result_endpoint == expected_endpoint
