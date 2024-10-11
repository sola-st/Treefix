# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH-24559
val = np.datetime64("2000-01-01 00:00:00", "ns")
values = np.array([val.view("i8")])

result = DatetimeIndex(values).tz_localize("US/Central")

expected = DatetimeIndex(["2000-01-01T00:00:00"], tz="US/Central")
tm.assert_index_equal(result, expected)

# but UTC is *not* deprecated.
with tm.assert_produces_warning(None):
    result = DatetimeIndex(values, tz="UTC")
expected = DatetimeIndex(["2000-01-01T00:00:00"], tz="US/Central")
