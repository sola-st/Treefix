# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_join.py
# GH#32157
dti = date_range("2016-01-01", periods=10, tz=tz)
result = dti[:5].join(dti[5:], how="outer")
assert result.freq == dti.freq
tm.assert_index_equal(result, dti)

result = dti[:5].join(dti[6:], how="outer")
assert result.freq is None
expected = dti.delete(5)
tm.assert_index_equal(result, expected)
