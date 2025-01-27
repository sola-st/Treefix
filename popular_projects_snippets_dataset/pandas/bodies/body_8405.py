# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
dr = date_range(start, end, freq="D")
assert dr[0] == start
assert dr[-1] == end
assert np.all(dr.hour == 0)

dr = date_range(start, end, freq="D", tz="US/Eastern")
assert dr[0] == start
assert dr[-1] == end
assert np.all(dr.hour == 0)

dr = date_range(
    start.replace(tzinfo=None),
    end.replace(tzinfo=None),
    freq="D",
    tz="US/Eastern",
)
assert dr[0] == start
assert dr[-1] == end
assert np.all(dr.hour == 0)
