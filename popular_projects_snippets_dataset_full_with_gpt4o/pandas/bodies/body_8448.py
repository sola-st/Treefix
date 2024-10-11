# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
msg = "'unit' must be one of 's', 'ms', 'us', 'ns'"
with pytest.raises(ValueError, match=msg):
    date_range("2016-01-01", "2016-03-04", periods=3, unit="h")
