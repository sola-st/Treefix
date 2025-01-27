# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#24252 avoid doing unnecessary addition that _would_ overflow
start = Timestamp.max.floor("D").to_pydatetime()
rng = date_range(start, end=None, periods=1, freq="B")
expected = DatetimeIndex([start], freq="B")
tm.assert_index_equal(rng, expected)
