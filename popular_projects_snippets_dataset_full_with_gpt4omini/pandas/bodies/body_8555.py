# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
tz = tz_aware_fixture
i = date_range("20130101", periods=5, freq="H", tz=tz)
kwargs = {key: attrgetter(val)(i) for key, val in kwargs.items()}
result = DatetimeIndex(i, **kwargs)
tm.assert_index_equal(i, result)
