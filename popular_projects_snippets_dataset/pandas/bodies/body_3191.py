# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asof.py
# GH#16063 was casting bools to floats
dti = date_range("2017-01-01", freq="MS", periods=4)
ser = Series([True, False, True], index=dti[:-1])

ts = dti[-1]
res = ser.asof([ts])

expected = Series([True], index=[ts])
tm.assert_series_equal(res, expected)
