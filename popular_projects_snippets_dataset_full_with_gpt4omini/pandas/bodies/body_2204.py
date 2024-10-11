# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#27733
dti = date_range("2015-04-05", periods=3).rename("foo")
expected = dti.tz_localize("UTC")

obj = klass(dti)
expected = klass(expected)

result = to_datetime(obj, utc=True)
tm.assert_equal(result, expected)
