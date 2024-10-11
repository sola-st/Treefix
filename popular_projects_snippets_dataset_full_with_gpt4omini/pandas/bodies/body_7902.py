# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_resolution.py
idx = pd.period_range(start="2013-04-01", periods=30, freq=freq)
assert idx.resolution == expected
