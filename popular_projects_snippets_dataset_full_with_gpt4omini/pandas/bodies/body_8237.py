# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_period.py
ts = date_range("1/1/2000", "2/1/2000", tz=tz)

with tm.assert_produces_warning(UserWarning):
    # GH#21333 warning that timezone info will be lost
    # filter warning about freq deprecation

    result = ts.to_period()[0]
    expected = ts[0].to_period(ts.freq)

assert result == expected

expected = date_range("1/1/2000", "2/1/2000").to_period()

with tm.assert_produces_warning(UserWarning):
    # GH#21333 warning that timezone info will be lost
    result = ts.to_period(ts.freq)

tm.assert_index_equal(result, expected)
