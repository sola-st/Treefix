# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#1778

# Standard -> Daylight Savings Time
dr = date_range("03/06/2012 00:00", periods=200, freq="W-FRI", tz="US/Eastern")

assert (dr.hour == 0).all()

dr = date_range("2012-11-02", periods=10, tz=tzstr)
result = dr.hour
expected = pd.Index([0] * 10, dtype="int32")
tm.assert_index_equal(result, expected)
