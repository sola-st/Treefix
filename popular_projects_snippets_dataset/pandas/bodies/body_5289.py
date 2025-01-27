# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH #13346
period = TestPeriodProperties._period_constructor(bound, -offset)
expected = period.to_timestamp().round(freq="S")
assert getattr(period, period_property).round(freq="S") == expected
expected = (bound - offset * Timedelta(1, unit="S")).floor("S")
assert getattr(period, period_property).floor("S") == expected
