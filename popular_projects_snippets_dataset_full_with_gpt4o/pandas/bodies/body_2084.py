# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#32264
# GH#48969
value = np.str_("2019-02-04 10:18:46.297000+0000")

ser = Series([value])

exp = Timestamp("2019-02-04 10:18:46.297000", tz="UTC")

assert to_datetime(value) == exp
assert to_datetime(ser.iloc[0]) == exp

res = to_datetime([value])
expected = Index([exp])
tm.assert_index_equal(res, expected)

res = to_datetime(ser)
expected = Series(expected)
tm.assert_series_equal(res, expected)
