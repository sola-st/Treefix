# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# see GH#7758: A bit of magic is required to set
# default encoding to utf-8
digits = string.digits
test_series = [
    Series([digits * 10, tm.rands(63), tm.rands(64), tm.rands(1000)]),
    Series(["データーサイエンス、お前はもう死んでいる"]),
]

former_encoding = None

if sys.getdefaultencoding() == "utf-8":
    test_series.append(Series(["野菜食べないとやばい".encode()]))

for ser in test_series:
    res = ser.astype("unicode")
    expec = ser.map(str)
    tm.assert_series_equal(res, expec)

# Restore the former encoding
if former_encoding is not None and former_encoding != "utf-8":
    reload(sys)
    sys.setdefaultencoding(former_encoding)
