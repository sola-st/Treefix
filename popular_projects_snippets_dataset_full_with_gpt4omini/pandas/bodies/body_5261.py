# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# bugs in scikits.timeseries
freq = f"Q-{month}"
exp = Period("1989Q3", freq=freq)
assert "1989Q3" in str(exp)
stamp = exp.to_timestamp("D", how="end")
p = Period(stamp, freq=freq)
assert p == exp

stamp = exp.to_timestamp("3D", how="end")
p = Period(stamp, freq=freq)
assert p == exp
