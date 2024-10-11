# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_datetime.py
ts = rand_series_with_duplicate_datetimeindex

uniques = ts.index.unique()
for date in uniques:
    result = ts[date]

    mask = ts.index == date
    total = (ts.index == date).sum()
    expected = ts[mask]
    if total > 1:
        tm.assert_series_equal(result, expected)
    else:
        tm.assert_almost_equal(result, expected[0])

    cp = ts.copy()
    cp[date] = 0
    expected = Series(np.where(mask, 0, ts), index=ts.index)
    tm.assert_series_equal(cp, expected)

key = datetime(2000, 1, 6)
with pytest.raises(KeyError, match=re.escape(repr(key))):
    ts[key]

# new index
ts[datetime(2000, 1, 6)] = 0
assert ts[datetime(2000, 1, 6)] == 0
