# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
ts = Timestamp("2011-01-01 9:00:00.123456789")

# Warn the user of data loss (nanoseconds).
with tm.assert_produces_warning(UserWarning):
    expected = datetime(2011, 1, 1, 9, 0, 0, 123456)
    result = ts.to_pydatetime()
    assert result == expected
