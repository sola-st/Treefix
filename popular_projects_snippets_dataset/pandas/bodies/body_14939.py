# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
rtol = 10**-9
dateindex = tm.makeDateIndex(k=10, freq=freq)
rs = dtc.convert(dateindex, None, None)
xp = converter.mdates.date2num(dateindex._mpl_repr())
tm.assert_almost_equal(rs, xp, rtol=rtol)
