# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
rtol = 0.5 * 10**-9

rs = dtc.convert(Timestamp("2012-1-1 01:02:03", tz="UTC"), None, None)
xp = converter.mdates.date2num(Timestamp("2012-1-1 01:02:03", tz="UTC"))
tm.assert_almost_equal(rs, xp, rtol=rtol)

rs = dtc.convert(
    Timestamp("2012-1-1 09:02:03", tz="Asia/Hong_Kong"), None, None
)
tm.assert_almost_equal(rs, xp, rtol=rtol)

rs = dtc.convert(datetime(2012, 1, 1, 1, 2, 3), None, None)
tm.assert_almost_equal(rs, xp, rtol=rtol)
