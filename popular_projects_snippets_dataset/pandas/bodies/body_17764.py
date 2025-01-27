# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
index = date_range("2013-11-03", periods=5, freq="3H").tz_localize(
    "America/Chicago"
)
assert index.inferred_freq is None
