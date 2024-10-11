# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH#7207, GH#11128
# test .dt namespace accessor

# periodindex
pi = period_range("20130101", periods=5, freq="D")
ser = Series(pi, name="xxx")

for prop in ok_for_period:
    # we test freq below
    if prop != "freq":
        self._compare(ser, prop)

for prop in ok_for_period_methods:
    getattr(ser.dt, prop)

freq_result = ser.dt.freq
assert freq_result == PeriodIndex(ser.values).freq
