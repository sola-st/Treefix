# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
rng = date_range("1/1/1850", "1/1/1950", freq="A-DEC")
rng.format()
ts = Series(1, index=rng)
repr(ts)
