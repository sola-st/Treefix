# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# bugs in scikits.timeseries
freq = f"A-{month}"
exp = Period("1989", freq=freq)
stamp = exp.to_timestamp("D", how="end") + timedelta(days=30)
p = Period(stamp, freq=freq)

assert p == exp + 1
assert isinstance(p, Period)
