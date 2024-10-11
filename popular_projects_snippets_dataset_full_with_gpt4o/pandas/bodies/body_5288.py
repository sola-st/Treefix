# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH #13346
period = TestPeriodProperties._period_constructor(bound, offset)
with pytest.raises(OutOfBoundsDatetime, match="Out of bounds nanosecond"):
    getattr(period, period_property)
