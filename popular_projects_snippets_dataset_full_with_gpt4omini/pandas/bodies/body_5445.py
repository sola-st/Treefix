# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# Ensure that converting to datetime and back only loses precision
# by going from nanoseconds to microseconds.
exp_warning = None if Timestamp.max.nanosecond == 0 else UserWarning
with tm.assert_produces_warning(exp_warning):
    pydt_max = Timestamp.max.to_pydatetime()

assert (
    Timestamp(pydt_max).as_unit("ns").value / 1000 == Timestamp.max.value / 1000
)

exp_warning = None if Timestamp.min.nanosecond == 0 else UserWarning
with tm.assert_produces_warning(exp_warning):
    pydt_min = Timestamp.min.to_pydatetime()

# The next assertion can be enabled once GH#39221 is merged
#  assert pydt_min < Timestamp.min  # this is bc nanos are dropped
tdus = timedelta(microseconds=1)
assert pydt_min + tdus > Timestamp.min

assert (
    Timestamp(pydt_min + tdus).as_unit("ns").value / 1000
    == Timestamp.min.value / 1000
)
