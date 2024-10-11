# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_to_timestamp.py
index = period_range("1/1/2012", periods=4, freq="D")

result = index.to_timestamp()
assert result[0] == Timestamp("1/1/2012")
