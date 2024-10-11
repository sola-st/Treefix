# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
rng = period_range("1959Q2", "2009Q3", freq=freq)
rng = Index(rng.to_timestamp("D", how="e").astype(object))

assert rng.inferred_freq == expected
