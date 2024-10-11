# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_period.py
# GH#22905
ts = date_range("1/1/2000", "2/1/2000", tz="Etc/GMT-1")
with tm.assert_produces_warning(UserWarning):

    result = ts.to_period()[0]
    expected = ts[0].to_period(ts.freq)
    assert result == expected
