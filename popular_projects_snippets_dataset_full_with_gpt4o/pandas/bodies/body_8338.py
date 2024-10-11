# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
tz = tz_naive_fixture
rng = date_range(start="2016-01-01", periods=5, freq="30Min", tz=tz)
elt = rng[1]

expected_rng = DatetimeIndex(
    [
        Timestamp("2016-01-01 00:00:00", tz=tz),
        Timestamp("2016-01-01 00:00:00", tz=tz),
        Timestamp("2016-01-01 01:00:00", tz=tz),
        Timestamp("2016-01-01 02:00:00", tz=tz),
        Timestamp("2016-01-01 02:00:00", tz=tz),
    ]
)
expected_elt = expected_rng[1]

tm.assert_index_equal(rng.round(freq="H"), expected_rng)
assert elt.round(freq="H") == expected_elt

msg = INVALID_FREQ_ERR_MSG
with pytest.raises(ValueError, match=msg):
    rng.round(freq="foo")
with pytest.raises(ValueError, match=msg):
    elt.round(freq="foo")

msg = "<MonthEnd> is a non-fixed frequency"
with pytest.raises(ValueError, match=msg):
    rng.round(freq="M")
with pytest.raises(ValueError, match=msg):
    elt.round(freq="M")

# GH#14440 & GH#15578
index = DatetimeIndex(["2016-10-17 12:00:00.0015"], tz=tz)
result = index.round("ms")
expected = DatetimeIndex(["2016-10-17 12:00:00.002000"], tz=tz)
tm.assert_index_equal(result, expected)

for freq in ["us", "ns"]:
    tm.assert_index_equal(index, index.round(freq))

index = DatetimeIndex(["2016-10-17 12:00:00.00149"], tz=tz)
result = index.round("ms")
expected = DatetimeIndex(["2016-10-17 12:00:00.001000"], tz=tz)
tm.assert_index_equal(result, expected)

index = DatetimeIndex(["2016-10-17 12:00:00.001501031"])
result = index.round("10ns")
expected = DatetimeIndex(["2016-10-17 12:00:00.001501030"])
tm.assert_index_equal(result, expected)

with tm.assert_produces_warning(False):
    ts = "2016-10-17 12:00:00.001501031"
    DatetimeIndex([ts]).round("1010ns")
