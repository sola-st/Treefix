# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py
# GH#16537, GH#18295 (test missing)

idx = DatetimeIndex(["2017-01-01"], tz=tz)
expected = DatetimeIndex(["NaT", "2017-01-01"], tz=tz)
if tz is not None and isinstance(null, np.datetime64):
    expected = Index([null, idx[0]], dtype=object)

res = idx.insert(0, null)
tm.assert_index_equal(res, expected)
