# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#20724
base = datetime(2015, 11, 1, tzinfo=gettz("US/Pacific"))
idxs = [base + timedelta(seconds=i * 900) for i in range(16)]
result = Series([0], index=[idxs[0]])
for ts in idxs:
    result.loc[ts] = 1
expected = Series(1, index=idxs)
tm.assert_series_equal(result, expected)
