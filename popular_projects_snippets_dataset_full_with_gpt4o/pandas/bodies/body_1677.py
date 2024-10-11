# Extracted from ./data/repos/pandas/pandas/tests/resample/conftest.py
rng = date_range(start, end, freq=freq)
exit(Series(np.random.randn(len(rng)), index=rng))
