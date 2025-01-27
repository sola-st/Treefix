# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
# 2579
values = [date(1677, 1, 1), date(1677, 1, 2)]
rs = dtc.convert(values, None, None)
xp = converter.mdates.date2num(values)
tm.assert_numpy_array_equal(rs, xp)
rs = dtc.convert(values[0], None, None)
xp = converter.mdates.date2num(values[0])
assert rs == xp

values = [datetime(1677, 1, 1, 12), datetime(1677, 1, 2, 12)]
rs = dtc.convert(values, None, None)
xp = converter.mdates.date2num(values)
tm.assert_numpy_array_equal(rs, xp)
rs = dtc.convert(values[0], None, None)
xp = converter.mdates.date2num(values[0])
assert rs == xp
