# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#21610, GH#22163 ensure DataFrame doesn't return object-dtype
tz = tz_aware_fixture
if tz == "US/Pacific":
    dates = date_range("2012-11-01", periods=3, tz=tz)
    offset = dates + pd.offsets.Hour(5)
    assert dates[0] + pd.offsets.Hour(5) == offset[0]

dates = date_range("2010-11-01 00:00", periods=3, tz=tz, freq="H")
expected = DatetimeIndex(
    ["2010-11-01 05:00", "2010-11-01 06:00", "2010-11-01 07:00"],
    freq="H",
    tz=tz,
)

dates = tm.box_expected(dates, box_with_array)
expected = tm.box_expected(expected, box_with_array)

for scalar in [pd.offsets.Hour(5), np.timedelta64(5, "h"), timedelta(hours=5)]:
    offset = dates + scalar
    tm.assert_equal(offset, expected)
    offset = scalar + dates
    tm.assert_equal(offset, expected)

    roundtrip = offset - scalar
    tm.assert_equal(roundtrip, dates)

    msg = "|".join(
        ["bad operand type for unary -", "cannot subtract DatetimeArray"]
    )
    with pytest.raises(TypeError, match=msg):
        scalar - dates
